#include <stdio.h>
#include <stdlib.h>    
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <sys/file.h>
#include <sys/socket.h> 
#include <netinet/in.h> 
#include <signal.h>     

#define PID_FILE  "/var/run/mydaemon.pid"
#define CONF_FILE "/etc/mydaemon.conf"
#define LOG_FILE  "/var/log/mydaemon.log"
#define PORT 8080     

volatile sig_atomic_t keep_running = 1;

void handle_signal(int signal) {
    if (signal == SIGTERM) {
        keep_running = 0;
    }
}

int main() {
    int fd, conf_fd, log_fd, sock_fd;
    char buf[128];
    struct sockaddr_in serv_addr;

    struct sigaction sa;
    sa.sa_handler = &handle_signal;
    sa.sa_flags = 0;
    sigemptyset(&sa.sa_mask);
    if (sigaction(SIGTERM, &sa, NULL) == -1) {
        perror("Sigaction Error");
        return 1;
    }


    printf("=== mydaemon start (PID: %d) ===\n", getpid());
    
    fd = open(PID_FILE, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
	    perror("PID Open Error"); 
	    return 1; 
	  }

    if (flock(fd, LOCK_EX | LOCK_NB) < 0) {
        printf("Error: Process already running.\n");
        return 1;
    }
    
    sprintf(buf, "%d\n", getpid());
    write(fd, buf, strlen(buf));
    printf("[OK] PID file locked and written.\n");


    conf_fd = open(CONF_FILE, O_RDONLY);
    if (conf_fd >= 0) {
        read(conf_fd, buf, sizeof(buf)); 
        close(conf_fd);
        printf("[OK] Config file read.\n");
    } else {
        printf("[SKIP] Config file not found (or permission denied).\n");
    }
    

    log_fd = open(LOG_FILE, O_WRONLY | O_CREAT | O_APPEND, 0644);
    if (log_fd >= 0) {
        char *msg = "mydaemon started successfully.\n";
        write(log_fd, msg, strlen(msg));
        close(log_fd);
        printf("[OK] Startup log written.\n");
    } else {
        perror("Startup Log Write Error");
    }

    
    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0) {
        perror("Socket Creation Error");
    } else {
        int opt = 1;
        setsockopt(sock_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));

        serv_addr.sin_family = AF_INET;
        serv_addr.sin_addr.s_addr = INADDR_ANY; 
        serv_addr.sin_port = htons(PORT);       

		
        if (bind(sock_fd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) {
            perror("Socket Bind Error");
        } else {
            if (listen(sock_fd, 3) < 0) {
                perror("Socket Listen Error");
            } else {
                printf("[OK] Socket bound to port %d and listening.\n", PORT);
            }
        }
    }
    
    printf("--- Waiting for SIGTERM (kill %d) to exit... ---\n", getpid());
    while (keep_running) {
        sleep(1);
    }
    printf("\n--- SIGTERM received. Cleaning up... ---\n");
		

    if (sock_fd >= 0) close(sock_fd);
    
    
    log_fd = open(LOG_FILE, O_WRONLY | O_CREAT | O_APPEND, 0644);
    if (log_fd >= 0) {
        char *msg = "mydaemon stopped safely.\n";
        write(log_fd, msg, strlen(msg));
        close(log_fd);
        printf("[OK] Log written.\n");
    } else {
        perror("Log Write Error");
    }
    
    if (unlink(PID_FILE) == 0) {
        printf("[OK] PID file removed.\n");
    } else {
        perror("PID Unlink Error");
    }

    close(fd); 

    printf("=== mydaemon finished ===\n");
    return 0;
}