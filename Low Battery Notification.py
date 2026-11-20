"""Low battery notification.

Checks the laptop battery every minute and shows a desktop
notification when the charge drops to or below a threshold
(default 20%) while the charger is unplugged.

Requires: psutil, plyer
    pip install psutil plyer
"""

import argparse
import time

try:
    import psutil
except ImportError:  # clear message instead of a bare traceback
    psutil = None

try:
    from plyer import notification
except ImportError:
    notification = None

LOW_BATTERY_THRESHOLD = 20
CHECK_INTERVAL_SECONDS = 60


def get_battery():
    """Return (percent, plugged) or None if this machine has no battery."""
    battery = psutil.sensors_battery()
    if battery is None:
        return None
    return battery.percent, battery.power_plugged


def alert(percent):
    """Show a desktop notification, falling back to the console."""
    message = f"Battery is at {percent}%. Please plug in your charger."
    if notification is not None:
        try:
            notification.notify(
                title="Low Battery",
                message=message,
                timeout=10,
            )
            return
        except Exception:
            pass
    print(f"Low Battery: {message}")


def check_once(threshold):
    """Check the battery a single time. Returns True if an alert fired."""
    status = get_battery()
    if status is None:
        print("No battery detected on this machine.")
        return False
    percent, plugged = status
    print(f"Battery: {percent}% | {'Charging' if plugged else 'Discharging'}")
    if not plugged and percent <= threshold:
        alert(percent)
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Warn when the battery runs low.")
    parser.add_argument("--threshold", type=int, default=LOW_BATTERY_THRESHOLD,
                        help="alert at or below this battery percent (default: 20)")
    parser.add_argument("--once", action="store_true",
                        help="check once and exit instead of watching")
    parser.add_argument("--interval", type=int, default=CHECK_INTERVAL_SECONDS,
                        help="seconds between checks when watching (default: 60)")
    args = parser.parse_args()

    if psutil is None:
        print("psutil is not installed. Run: pip install psutil plyer")
        return

    if args.once:
        check_once(args.threshold)
        return

    alerted = False
    try:
        while True:
            status = get_battery()
            if status is None:
                print("No battery detected on this machine.")
                return
            percent, plugged = status
            if not plugged and percent <= args.threshold and not alerted:
                alert(percent)
                alerted = True
            elif plugged or percent > args.threshold:
                alerted = False
            print(f"Battery: {percent}% | {'Charging' if plugged else 'Discharging'}")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Stopped by user.")


if __name__ == "__main__":
    main()
