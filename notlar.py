gst-launch-1.0 -e -v udpsrc src=192.168.2.146 port=5900 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjitterbuffer ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink



gst-launch-1.0 -v ximagesrc  ! queue  ! videoconvert !  video/x-raw,format=I420 ! jpegenc ! rtpjpegpay ! queue ! udpsink host=127.0.0.1 port=5900





gst-launch-1.0 -v ximagesrc  ! queue  ! videoconvert !  video/x-raw,format=I420 ! jpegenc ! rtpjpegpay ! queue ! udpsink host=192.168.2.53 port=5900

gst-launch-1.0 -e -v udpsrc port=5900 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjitterbuffer ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink

gst-launch-1.0 udpsrc port=5900 ! application/x-rtp, encoding-name=JPEG,payload=26 ! rtpjitterbuffer ! rtpjpegdepay ! jpegparse ! jpegdec ! autovideosink



gst-launch-1.0 rtspsink name=sink service=$12345 \
v4l2src ! x264enc ! h264parse ! capsfilter caps="video/x-h264, mapping=${/stream}" ! sink. \
alsasrc ! voaacenc ! aacparse ! capsfilter caps="audio/mpeg, mapping=${/stream}" ! sink.

###########################################################################################


ffmpeg -f pulse -ac 2 -i 0 -f x11grab -rtbufsize 100M -s 1200x720 -framerate 30 -probesize 10M -draw_mouse 1 -i :0.0 -acodec aac -c:v libx264 -r 30 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p -f flv rtmp://demo.flashphoner.com:1935/live/rtmp_stream

ffmpeg -f pulse -ac 2 -i 0 -f x11grab -rtbufsize 100M -s 1920x1080 -framerate 30 -probesize 10M -draw_mouse 1 -i :0.0 -acodec aac -c:v libx264 -r 30 -preset ultrafast -tune zerolatency -crf 25 -pix_fmt yuv420p -f mpegts udp://192.168.2.53:6666?pkt_size=1316

ffmpeg -video_size 1920x1080 -framerate 25 -f x11grab -i :0.0 -f mpegts udp://192.168.2.53:6666?pkt_size=2000

ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 -f mpegts udp://192.168.2.55:6666?pkt_size=2000

#screencapture
ffmpeg -threads 6 -video_size 1920x1080 -framerate 15 -f x11grab -i :0.0 -preset ultrafast -tune zerolatency -f mpegts udp://192.168.2.55:6666?pkt_size=2000


###########################################################################################
gst-launch-1.0 v4l2src device=/dev/video0 ! image/jpeg, width=640, height=480, framerate=15/1 ! jpegdec ! avenc_mpeg2video idct-algo=7 dct-algo=0 bitrate=750000 bitrate-tolerance=4000000 ! multiudpsink clients=192.168.2.3:5400,192.168.2.55:5400 async=false

gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-h264,width=640,height=480,framerate=30/1 ! mpegtsmux ! multiudpsink clients=192.168.2.53:5400,192.168.2.55:5400 async=false

ffmpeg -f v4l2 -i video="USB Camera" -f alsa -i hw:0 -profile:v high -pix_fmt yuvj420p -level:v 4.1 -preset ultrafast -tune zerolatency -vcodec libx264 -r 10 -b:v 512k -s 640x360 -acodec aac -strict -2 -ac 2 -ab 32k -ar 44100 -f mpegts -flush_packets 0 udp://192.168.2.55:5400?pkt_size=1316


gst-launch-1.0 v4l2src device="/dev/video0" ! \
"video/x-raw, width=640, height=480, format=(string)YUY2" ! \
udpsink host=192.168.2.55 port=5400

gst-launch-1.0 alsasrc name=audiosrc ! audio/x-raw, rate=8000, channels=1, format=S16LE ! alawenc hard-resync=true ! rtppcmapay max-ptime=-1 mtu=1400 ! multiudpsink clients=192.168.2.3:5800,192.168.2.55:5800 async=false
###########################################################################################

#android için gerekli ayarlı streamler
gst-launch-1.0 v4l2src device=/dev/video0 ! image/jpeg, width=640, height=480, framerate=20/1 ! jpegdec ! avenc_mpeg2video idct-algo=7 dct-algo=0 bitrate=500000 bitrate-tolerance=4000000 ! multiudpsink clients=192.168.2.3:5400,192.168.2.55:5400 async=false 

gst-launch-1.0 v4l2src device=/dev/video0 ! image/jpeg, width=320, height=240, framerate=25/1 ! jpegdec ! avenc_mpeg2video idct-algo=7 dct-algo=0 bitrate-tolerance=4000000 ! multiudpsink clients=192.168.2.3:5400,192.168.2.55:5400 async=false 

gst-launch-1.0 v4l2src device=/dev/video0 ! image/jpeg, width=640, height=320, framerate=15/1 ! jpegdec ! avenc_mpeg2video idct-algo=7 dct-algo=0 bitrate=750000 bitrate-tolerance=4000000 ! multiudpsink clients=192.168.2.3:5400,192.168.2.55:5400 async=false

###########################################################################################

#donanımları görmek için 
v4l2-ctl -d /dev/video0 --list-formats-ext

1515

nmcli dev wifi hotspot ifname wlp4s0 ssid test password "test1234"

E3m5s76060
###########################################################################################

#hotspot
nmcli con add type wifi ifname wlan0 con-name Hotspotukb1 autoconnect yes ssid Hotspotukb1 \
nmcli con modify Hotspotukb1 802-11-wireless.mode ap 802-11-wireless.band bg ipv4.method shared \
nmcli con modify Hotspotukb1 wifi-sec.key-mgmt wpa-psk \
nmcli con modify Hotspotukb1 wifi-sec.psk "test1234" \
nmcli con up Hostspotukb

###########################################################################################

gst-launch-1.0 rtspsrc location=rtsp://admin:esetron16@192.168.2.5:554/cam/realmonitor?channel=1&subtype=0 name=src \
src. ! rtph264depay ! h264parse ! avdec_h264 ! queue ! autovideosink \
src. ! rtpmp4adepay ! aacparse ! avdec_aac ! queue ! autoaudiosink

###########################################################################################
#raspberry permission verir
sudo chown -R pi:pi /home/pi/ika/classes/

###########################################################################################

#dene bridge için
iw dev wlan0 set 4addr on
###########################################################################################
#ikadan gelen görüntüyü dağıtmak için 
pipe_str = \
            ' udpsrc name=videosrc port=' + str(UKBParams.videoStreamPort) + \
            ' ! video/mpeg, width=640, height=480, framerate=15/1, mpegversion=2 ' \
            ' ! tee name=t t.' \
            ' ! queue leaky=1 ' \
            ' ! udpsink host=10.42.0.51 port=5400 t. ' \
            ' ! queue leaky=1 ' \
            ' ! avdec_mpeg2video '
###########################################################################################
#yeni bullet takılırsa.
ssh -v user@hostname
###########################################################################################
#subprocess sonuna & koy backgroundprocess için
###########################################################################################
#android sutdioda token acceste gist kısmını açarsan android studiodan erişebilirsin.
repo - select everything
gist - select everything
org - select only read:org
###########################################################################################
#raspberry bootloaderscreen removed

STEP1: log into your Raspberry Pi via Terminal SSH (i used PuTTy) default login is pi .. password is raspberry

STEP2: type (or copy'n'paste) this
vcgencmd bootloader_version
to display the version and date of the bootloader you are using. eg. mine is Sep 3 2020 13:11:43

STEP3: type (or copy'n'paste) this (if your bootloader date is different to mine, then you'll need to change pieeprom-2020-09-03.bin to the date of your bootloader. format is YYYY/MM/DD)

cp /lib/firmware/raspberrypi/bootloader/beta/pieeprom-2020-09-03.bin pieeprom.bin

STEP4: type (or copy'n'paste) this
rpi-eeprom-config pieeprom.bin > config.txt

STEP5: type (or copy'n'paste) this
cat config.txt

STEP6: you should see something like this below ... and what you need to change is DISABLE_HDMI=0 to DISABLE_HDMI=1

BOOT_UART=0
WAKE_ON_GPIO=1
POWER_OFF_ON_HALT=0
DHCP_TIMEOUT=45000
DHCP_REQ_TIMEOUT=4000
TFTP_FILE_TIMEOUT=30000
ENABLE_SELF_UPDATE=1
DISABLE_HDMI=0
BOOT_ORDER=0xf41

STEP7: type (or copy'n'paste) this
sudo nano config.txt

STEP8: edit DISABLE_HDMI=0 to DISABLE_HDMI=1 .. then on your keyboard press CTRL O, then ENTER, then Y, and then CTRL X

STEP9: type (or copy'n'paste) this
rpi-eeprom-config --out pieeprom-out.bin --config config.txt pieeprom.bin

STEP10: type (or copy'n'paste) this
sudo rpi-eeprom-update -d -f ./pieeprom-out.bin

STEP11: You will now see the following message

BCM2711 detected Dedicated VL805 EEPROM detected *** INSTALLING ./pieeprom-out.bin *** BOOTFS /boot EEPROM update pending. Please reboot to apply the update.

STEP12: Last Step .. type
sudo reboot


###########################################################################################
















