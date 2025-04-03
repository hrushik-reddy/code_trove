

- docker
    ```bash
    sudo docker build -t newcont .
    ```
    1. docker command to stop all containers
        ```bash
        sudo docker stop $(sudo docker ps -a -q)
        ```
    2. docker command to remove all images
        ```bash
        sudo docker rmi $(sudo docker images -q)
        ```
    3. docker command to stop all containers and remove all images
        ```bash
        sudo docker stop $(sudo docker ps -a -q) && sudo docker rmi $(sudo docker images -q) && sudo docker system prune -a
        ```
    4. docker command to view container logs
        ```bash
        sudo docker logs -f <container_id>
        ```
    5. docker command to execute commands in a running container
        ```bash
        sudo docker exec -it <container_id> /bin/bash
        ```
- linux commands
    1. copy and move
        ```bash
        cp source destination
        mv source destination
        ```
    2. zip a file
        ```bash
        zip -r <destination_file_name> <source_folder>
        ```
    3. add a ssh key into a vm
        ```bash
        ssh-keygen
        cat ~/.ssh/id_ed25519.pub
        cat ~/.ssh/id_rsa.pub
        ```
        ```bash
        type C:\Users\Techolution\.ssh\id_ed25519.pub   # for windows
        ```
        ```bash
        echo "<ssh key>" >> ~/.ssh/authorized_keys
        chmod 600 ~/.ssh/authorized_keys
        ```
        ```bash
        curl ifconfig.me
        ```
    4. to check storage and free ram
        ```bash
        df -h
        free -h
        top
        htop
        ```
    5. kill ports (with mercy)
        ```bash
        sudo lsof -i:<port>
        sudo kill -9 <port>
        ```
    6. kill ports (without mercy)
        ```bash
        sudo fuser -k <port>/tcp
        ```
    7. ufw
        ```bash
        ufw allow <port>
        ```
    8. find files by name or content
        ```bash
        find /path/to/search -name "filename*"
        grep -r "search_text" /path/to/search
        ```
    9. monitor system performance in real-time
        ```bash
        vmstat 1
        iostat -xz 1
        ```
    10. create and manage symbolic links
        ```bash
        ln -s /path/to/original /path/to/link
        ```
    11. manage systemd services
        ```bash
        sudo systemctl start|stop|restart|status <service_name>
        sudo systemctl enable|disable <service_name>
        ```
