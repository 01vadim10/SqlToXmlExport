import sys
import main

try:
    args = sys.argv
    exit_code = main.main(args)
    sys.exit(exit_code)
except EnvironmentError as error:
    sys.stderr.write(str(error))
    sys.exit(1)
except KeyboardInterrupt as error:
    sys.exit(2)
except Exception as error:
    sys.stderr.write(str(error))
    sys.exit(3)
