# Street Light Gateway Data Processor

## Introduction

This project is about an IoT gateway data processor, mainly communicate with street lights devices.

Showing two features:

- Receiving Run-time street light data, transfer and saving into database.
- Making operation command (adjust light dimming) to street light IoT devices.

Purpose:

- To show `design` and `implement` of communication with IoT devices. 


## System Design Explanation

In this project, I can not really rent several street lights for demo, so I will make some data simulation programs 
for simulating data of street lights send from devices to our project.

Also making another simulation program for supposing there are people use website to manage these lights
 and send command to those street lights for adjusting the dimming value.

The next two photos are the structure of this project. 

![](https://minayu0416.files.wordpress.com/2021/03/screen-shot-2021-03-09-at-2.52.45-pm.png)

`MQTT` is a network protocol like HTTP, but it is most common used for IoT devices. In this photo, 
we can see how those street lights (devices) communicate to our programs.

Hardware programmers will put `micro computer`, such as `Raspberry Pi` into each devices, 
then sending data through `MQTT` publish to specific topic (in this case the topic is `/com/device/msg/{device_id}`),
 then our project activate `MQTT` subscribe the topic (`/com/device/msg/*`) for getting those data from devices.


![](https://minayu0416.files.wordpress.com/2021/03/screen-shot-2021-03-09-at-2.52.59-pm.png)

About sending command to devices, in same theory. In project, composing those command, transfer to specific format then
 publish to specific topic (`/com/device/command/{device_id}`), then each devices subscribe its topic will receive command
  from programs.     

**More detail information will be write in my blog articles in the future.**
