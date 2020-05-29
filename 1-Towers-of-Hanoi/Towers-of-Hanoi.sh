#!/usr/bin/sh

style(){
    case $1 in 
        LEFT)
            echo "\033[0;31m"
        ;;
        MIDDLE)
            echo "\033[0;34m"
        ;;
        RIGHT)
            echo "\033[0;32m"
        ;;
    esac
}

noStyle="\033[0m"
hanoi(){
    if (( $1 <= 0 ))
    then
        return
    fi
    local LEFT=${2:-'LEFT'}
    local RIGHT=${3:-'RIGHT'}
    local MIDDLE=${4:-'MIDDLE'}
    local NEW_HEIGHT=$1-1
    leftStyle=$( style $LEFT )
    rightStyle=$( style $RIGHT )

    hanoi $NEW_HEIGHT $LEFT $MIDDLE $RIGHT
    printf "%b %s %b %s %b %s %b\n" "$leftStyle $LEFT $noStyle => $rightStyle $RIGHT $noStyle"
    #echo "$leftStyle $LEFT $noStyle => $rightStyle $RIGHT $noStyle"
    hanoi $NEW_HEIGHT $MIDDLE $RIGHT $LEFT
}

TOWER_SIZE=${1:-3}
hanoi $TOWER_SIZE