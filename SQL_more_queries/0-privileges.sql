#!/bin/bash
"""hello"""
for user in user_0d_1 user_0d_2; do
    echo "Grants for $user@localhost:"
    mysql -hlocalhost -uroot -p -e "SHOW GRANTS FOR '$user'@'localhost';"
    echo "------------------------------------"
done
