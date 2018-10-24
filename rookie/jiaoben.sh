#!/bin/bash

while :
do
    echo "  menu  "
    echo "选择1,查系统"
    echo "选择2,查内存"
    echo ""
    read -p "输入1或者2,输入其他退出： " choice
    echo ""
    case $choice in
    1)
            cat /etc/issue
            read -p "任意键继续"
            echo ""
            ;;
    2)
            free -m 
            echo ""
            read -p "任意键继续"
            echo "" 
            ;;
    *)
            echo "BYE"
            exit 0
            ;;
    esac
done    

