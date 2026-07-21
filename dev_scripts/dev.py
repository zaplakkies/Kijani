# Compiles & uploads code, then uploads static files in data directory
# Finally watches serial port
# Usage: pio run -t dev

Import("env")
import sys

def deploy_and_monitor(source, target, env):
    # Upload firmware
    result = env.Execute("pio run -t deploy")
    if result != 0:
        print("Deploy failed. Exiting.")
        sys.exit(result)

    # Monitor device
    result = env.Execute("pio device monitor")
    if result != 0:
        print("Monitoring failed. Exiting.")
        sys.exit(result)

# Register the custom target "deploy"
env.AddTarget("dev", None, deploy_and_monitor)
