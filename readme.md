### 监控任务进程

```
  在异步任务中， 任务进程进程有时候需要脱离主进程单独运行， 独立运行的程序需要拥有一种机制进行纳管。 这里提供一种在linux主机上监控进程是否存活的方法

example 提供注册监控进程的方法
```

#### 部署


```
mkdir -p /usr/local/unixMgr/

cp etc/unix_monitor_process.service /usr/lib/systemd/system/

systemctl enable unix_monitor_process.service
systemctl start unix_monitor_process.service
systemctl status unix_monitor_process.service
```

