#!/bin/sh

command=$1

case $command in
    "start")
        source myenv/Scripts/activate
        ;;
    "stop")
        deactivate
        ;;
    *)
        echo ""
        echo "Please enter one of the following commands only:"
        echo "* start"
        echo "* end"
        echo ""
        echo "And then, you must run this script with"
        echo ". /path/to/this/script/venv.sh \$COMMAND"
        ;;
esac
