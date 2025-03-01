# Nota

Para detalles en la construccion y pruebas de este taller anexo un snapshot de mi terminal de powershell (conectada a ubuntu via `ssh`), en ella se evidencia la creacion de los elementos y la primera implementación exitosa del sistema:

```powershell
Last login: Fri Feb 28 18:57:08 2025
san@UbuDesk:~$ dir
Desktop    Downloads         Music     Public  Templates
Documents  flask_docker_app  Pictures  snap    Videos
san@UbuDesk:~$ mkdir -p docker_compose_workshop
cd docker_compose_workshop
mkdir api
touch docker-compose.yml
san@UbuDesk:~/docker_compose_workshop$ nano docker-compose.yml
san@UbuDesk:~/docker_compose_workshop$ nano docker-compose.yml
san@UbuDesk:~/docker_compose_workshop$ cd api
touch app.py requirements.txt Dockerfile
san@UbuDesk:~/docker_compose_workshop/api$ nano Dockerfile
san@UbuDesk:~/docker_compose_workshop/api$ nano requirements.txt
san@UbuDesk:~/docker_compose_workshop/api$ nano app.py
san@UbuDesk:~/docker_compose_workshop/api$ cd ..  
docker-compose up -d
Command 'docker-compose' not found, but can be installed with:
snap install docker          # version 27.5.1, or
snap install docker          # version 27.2.0
apt  install docker-compose  # version 1.29.2-1
See 'snap info <snapname>' for additional versions.
san@UbuDesk:~/docker_compose_workshop$ sudo apt update
sudo apt install docker-compose
[sudo] password for san:
Get:1 https://download.docker.com/linux/ubuntu jammy InRelease [48,8 kB]
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Hit:3 http://us.archive.ubuntu.com/ubuntu jammy InRelease
Get:4 http://us.archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Get:5 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages [45,7 kB]
Get:6 http://us.archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:7 http://us.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [2.352 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/main i386 Packages [593 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [2.110 kB]
Get:10 http://us.archive.ubuntu.com/ubuntu jammy-updates/main i386 Packages [760 kB]
Get:11 http://us.archive.ubuntu.com/ubuntu jammy-updates/main Translation-en [392 kB]
Get:12 http://us.archive.ubuntu.com/ubuntu jammy-updates/main amd64 DEP-11 Metadata [103 kB]
Get:13 http://us.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [3.008 kB]
Get:14 http://security.ubuntu.com/ubuntu jammy-security/main Translation-en [329 kB]
Get:15 http://security.ubuntu.com/ubuntu jammy-security/main amd64 DEP-11 Metadata [43,1 kB]
Get:16 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [2.899 kB]
Get:17 http://us.archive.ubuntu.com/ubuntu jammy-updates/restricted Translation-en [528 kB]
Get:18 http://us.archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 DEP-11 Metadata [212 B]
Get:19 http://us.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1.192 kB]
Get:20 http://us.archive.ubuntu.com/ubuntu jammy-updates/universe i386 Packages [759 kB]
Get:21 http://us.archive.ubuntu.com/ubuntu jammy-updates/universe Translation-en [293 kB]
Get:22 http://us.archive.ubuntu.com/ubuntu jammy-updates/universe amd64 DEP-11 Metadata [359 kB]
Get:23 http://security.ubuntu.com/ubuntu jammy-security/restricted Translation-en [509 kB]
Get:24 http://us.archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 DEP-11 Metadata [940 B]
Get:25 http://us.archive.ubuntu.com/ubuntu jammy-backports/main amd64 DEP-11 Metadata [7.024 B]
Get:26 http://us.archive.ubuntu.com/ubuntu jammy-backports/restricted amd64 DEP-11 Metadata [216 B]
Get:27 http://us.archive.ubuntu.com/ubuntu jammy-backports/universe amd64 DEP-11 Metadata [17,8 kB]
Get:28 http://us.archive.ubuntu.com/ubuntu jammy-backports/multiverse amd64 DEP-11 Metadata [212 B]
Get:29 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 DEP-11 Metadata [208 B]
Get:30 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [965 kB]
Get:31 http://security.ubuntu.com/ubuntu jammy-security/universe i386 Packages [652 kB]
Get:32 http://security.ubuntu.com/ubuntu jammy-security/universe Translation-en [207 kB]
Get:33 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 DEP-11 Metadata [125 kB]
Get:34 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 DEP-11 Metadata [208 B]
Fetched 18,7 MB in 27s (686 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
374 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It iWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2210 (unattended-upgr)
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It iWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2210 (unattended-upgr)
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It iWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2210 (unattended-upgr)

...

Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It iWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2210 (unattended-upgr)
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It iWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2210 (unattended-upgr)
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It iWaiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It is held by process 2210 (unattended-upgr)
Waiting for cache lock: Could not get lock /var/lib/dpkg/lock-frontend. It i^Cheld by process 2210 (unattended-upgr)... 137s
san@UbuDesk:~/docker_compose_workshop$ sudo lsof /var/lib/dpkg/lock-frontend
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1000/gvfs
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1000/doc
      Output information may be incomplete.
COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
unattende 2210 root   10uW  REG    8,3        0 817293 /var/lib/dpkg/lock-frontend
san@UbuDesk:~/docker_compose_workshop$ sudo tail -f /var/log/unattended-upgrades/unattended-upgrades.log
2025-02-25 16:32:40,046 INFO Initial whitelist (not strict):
2025-02-25 16:55:39,148 INFO Packages that will be upgraded: accountsservice amd64-microcode apparmor apport apport-gtk avahi-autoipd avahi-daemon avahi-utils bash bind9-dnsutils bind9-host bind9-libs bluez bluez-cups bluez-obexd bsdextrautils bsdutils bubblewrap busybox-initramfs busybox-static cpio cups cups-browsed cups-bsd cups-client cups-common cups-core-drivers cups-daemon cups-filters cups-filters-core-drivers cups-ipp-utils cups-ppdc cups-server-common dbus dbus-user-session dirmngr distro-info-data dnsmasq-base dpkg espeak-ng-data evolution-data-server evolution-data-server-common fdisk file fonts-opensymbol gdb ghostscript ghostscript-x gir1.2-accountsservice-1.0 gir1.2-gdkpixbuf-2.0 gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-gtk-3.0 gir1.2-gtk-4.0 gir1.2-harfbuzz-0.0 gir1.2-javascriptcoregtk-4.0 gir1.2-mutter-10 gir1.2-rsvg-2.0 gir1.2-soup-2.4 gir1.2-vte-2.91 gir1.2-webkit2-4.0 gnome-control-center gnome-control-center-data gnome-control-center-faces gnome-shell gnome-shell-common gnupg gnupg-l10n gnupg-utils gpg gpg-agent gpg-wks-client gpg-wks-server gpgconf gpgsm gpgv gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps gstreamer1.0-plugins-good gstreamer1.0-pulseaudio gstreamer1.0-tools gstreamer1.0-x gtk-update-icon-cache gtk2-engines-pixbuf intel-microcode ipp-usb isc-dhcp-client isc-dhcp-common klibc-utils less libaccountsservice0 libapparmor1 libarchive13 libavahi-client3 libavahi-common-data libavahi-common3 libavahi-core7 libavahi-glib1 libavahi-ui-gtk3-0 libblkid1 libbluetooth3 libbpf0 libc-bin libc-dev-bin libc-devtools libc6 libc6-dbg libc6-dev libcamel-1.2-63 libcap2 libcap2-bin libcdio19 libcom-err2 libcue2 libcups2 libcupsfilters1 libcupsimage2 libcurl3-gnutls libdbus-1-3 libebackend-1.2-10 libebook-1.2-20 libebook-contacts-1.2-3 libecal-2.0-1 libedata-book-1.2-26 libedata-cal-2.0-1 libedataserver-1.2-26 libedataserverui-1.2-3 libespeak-ng1 libexempi8 libexpat1 libfdisk1 libflac8 libfontembed1 libfreerdp-client2-2 libfreerdp-server2-2 libfreerdp2-2 libfreetype6 libfribidi0 libgail-common libgail18 libgd3 libgdk-pixbuf-2.0-0 libgdk-pixbuf2.0-bin libgdk-pixbuf2.0-common libgif7 libglib2.0-0 libglib2.0-bin libglib2.0-data libgnutls30 libgs9 libgs9-common libgsf-1-114 libgsf-1-common libgssapi-krb5-2 libgstreamer-gl1.0-0 libgstreamer-plugins-base1.0-0 libgstreamer-plugins-good1.0-0 libgstreamer1.0-0 libgtk-3-0 libgtk-3-bin libgtk-3-common libgtk-4-1 libgtk-4-bin libgtk-4-common libgtk2.0-0 libgtk2.0-bin libgtk2.0-common libharfbuzz-icu0 libharfbuzz0b libhttp-daemon-perl libinput-bin libinput10 libjavascriptcoregtk-4.0-18 libjbig0 libjson-c5 libk5crypto3 libklibc libkpathsea6 libkrb5-3 libkrb5support0 libksba8 libldap-2.5-0 libldap-common libldb2 libllvm13 liblouis-data liblouis20 libmagic-mgc libmagic1 libmount1 libmozjs-91-0 libmpg123-0 libmutter-10-0 libnautilus-extension1a libncurses6 libncursesw6 libndp0 libnetplan0 libnghttp2-14 libnspr4 libnss-systemd libnss3 libntfs-3g89 libopenjp2-7 liborc-0.4-0 libpam-cap libpam-modules libpam-modules-bin libpam-runtime libpam-sss libpam-systemd libpam0g libpcre2-32-0 libpcre2-8-0 libpcre3 libperl5.34 libpixman-1-0 libpoppler-cpp0v5 libpoppler-glib8 libpoppler118 libprocps8 libprotobuf23 libpython3-stdlib libpython3.10 libpython3.10-minimal libpython3.10-stdlib libraw20 libreoffice-base-core libreoffice-calc libreoffice-core libreoffice-draw libreoffice-gnome libreoffice-gtk3 libreoffice-help-common libreoffice-help-en-us libreoffice-impress libreoffice-math libreoffice-ogltrans libreoffice-pdfimport libreoffice-style-breeze libreoffice-style-colibre libreoffice-style-elementary libreoffice-style-yaru libreoffice-writer librsvg2-2 librsvg2-common libsmartcols1 libsmbclient libsndfile1 libsnmp-base libsnmp40 libsoup-gnome2.4-1 libsoup2.4-1 libsoup2.4-common libsqlite3-0 libss2 libssh-4 libssl3 libsynctex2 libsysmetrics1 libsystemd0 libtasn1-6 libtiff5 libtinfo6 libtss2-esys-3.0.2-0 libtss2-mu0 libtss2-sys1 libtss2-tcti-cmd0 libtss2-tcti-device0 libtss2-tcti-mssim0 libtss2-tcti-swtpm0 libudev1 libuno-cppu3 libuno-cppuhelpergcc3-3 libuno-purpenvhelpergcc3-3 libuno-sal3 libuno-salhelpergcc3-3 libuuid1 libuv1 libvpx7 libvte-2.91-0 libvte-2.91-common libwayland-client0 libwayland-cursor0 libwayland-egl1 libwayland-server0 libwbclient0 libwebkit2gtk-4.0-37 libwebp7 libwebpdemux2 libwebpmux3 libwinpr2-2 libx11-6 libx11-data libx11-xcb1 libxml2 libxpm4 libxslt1.1 libyajl2 linux-firmware linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04 linux-image-generic-hwe-22.04 linux-libc-dev linux-tools-common locales login logrotate logsave mokutil mount mutter-common nano nautilus nautilus-data ncurses-base ncurses-bin netplan.io networkd-dispatcher ntfs-3g openssl openvpn orca passwd perl perl-base perl-modules-5.34 poppler-utils printer-driver-foo2zjs printer-driver-foo2zjs-common printer-driver-splix procps python3 python3-apport python3-cryptography python3-future python3-gdbm python3-idna python3-jwt python3-ldb python3-lib2to3 python3-louis python3-mako python3-minimal python3-oauthlib python3-paramiko python3-pil python3-pkg-resources python3-problem-report python3-protobuf python3-renderpm python3-reportlab python3-reportlab-accel python3-requests python3-uno python3-urllib3 python3-zipp python3.10 python3.10-minimal remmina remmina-common remmina-plugin-rdp remmina-plugin-secret remmina-plugin-vnc rfkill rsync rsyslog samba-libs snapd sudo systemd systemd-oomd systemd-sysv systemd-timesyncd tar thunderbird thunderbird-gnome-support thunderbird-locale-en tracker-extract tracker-miner-fs tzdata ubuntu-advantage-desktop-daemon ubuntu-drivers-common ubuntu-report udev uno-libs-private unzip ure util-linux uuid-runtime vim-common vim-tiny wget wireless-regdb wpasupplicant xserver-common xserver-xephyr xserver-xorg-core xserver-xorg-legacy xwayland xxd zlib1g
2025-02-25 16:55:39,151 INFO Writing dpkg log to /var/log/unattended-upgrades/unattended-upgrades-dpkg.log
2025-02-28 18:53:23,579 WARNING Could not figure out development release: Distribution data outdated. Please check for an update for distro-info-data. See /usr/share/doc/distro-info-data/README.Debian for details.
2025-02-28 18:53:23,580 INFO Starting unattended upgrades script
2025-02-28 18:53:23,580 INFO Allowed origins are: o=Ubuntu,a=jammy, o=Ubuntu,a=jammy-security, o=UbuntuESMApps,a=jammy-apps-security, o=UbuntuESM,a=jammy-infra-security
2025-02-28 18:53:23,580 INFO Initial blacklist:
2025-02-28 18:53:23,580 INFO Initial whitelist (not strict):
2025-02-28 18:57:05,777 INFO Packages that will be upgraded: accountsservice amd64-microcode apparmor apport apport-gtk avahi-autoipd bash bluez bluez-cups bluez-obexd bsdextrautils bsdutils bubblewrap busybox-initramfs cpio cups-filters cups-filters-core-drivers cups-ppdc dbus-user-session distro-info-data dnsmasq-base dpkg espeak-ng-data fdisk file gdb ghostscript ghostscript-x gir1.2-gdkpixbuf-2.0 gir1.2-gst-plugins-base-1.0 gir1.2-gstreamer-1.0 gir1.2-rsvg-2.0 gir1.2-vte-2.91 gnome-control-center gnome-control-center-data gnome-control-center-faces gnome-shell gnome-shell-common gstreamer1.0-alsa gstreamer1.0-gtk3 gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps gstreamer1.0-plugins-good gstreamer1.0-pulseaudio gstreamer1.0-tools gtk-update-icon-cache intel-microcode ipp-usb isc-dhcp-client klibc-utils less libaccountsservice0 libapparmor1 libarchive13 libblkid1 libbluetooth3 libbpf0 libc-bin libc-devtools libcap2 libcap2-bin libcdio19 libcom-err2 libcue2 libcupsfilters1 libcurl3-gnutls libespeak-ng1 libexpat1 libfdisk1 libflac8 libfontembed1 libfreetype6 libfribidi0 libgd3 libgdk-pixbuf-2.0-0 libgdk-pixbuf2.0-bin libgdk-pixbuf2.0-common libglib2.0-0 libglib2.0-bin libglib2.0-data libgnutls30 libgs9 libgs9-common libgsf-1-114 libgsf-1-common libgssapi-krb5-2 libgstreamer-gl1.0-0 libgstreamer-plugins-good1.0-0 libgstreamer1.0-0 libgtk-3-bin libgtk-4-bin libgtk2.0-common libharfbuzz0b libhttp-daemon-perl libinput-bin libinput10 libjbig0 libjson-c5 libk5crypto3 libklibc libkrb5-3 libkrb5support0 libksba8 libldap-2.5-0 libldap-common libldb2 libllvm13 liblouis-data libmagic-mgc libmagic1 libmount1 libmozjs-91-0 libmpg123-0 libnautilus-extension1a libncurses6 libncursesw6 libndp0 libnetplan0 libnghttp2-14 libnspr4 libnss3 libntfs-3g89 libopenjp2-7 liborc-0.4-0 libpam-runtime libpam-sss libpam0g libpcre2-32-0 libpcre2-8-0 libpcre3 libpixman-1-0 libpoppler-cpp0v5 libpoppler-glib8 libpoppler118 libprocps8 libprotobuf23 libpython3-stdlib libpython3.10 libpython3.10-minimal libpython3.10-stdlib libraw20 libreoffice-help-common libreoffice-help-en-us libreoffice-ogltrans libreoffice-pdfimport libreoffice-style-breeze libreoffice-style-elementary libreoffice-style-yaru libsmartcols1 libsmbclient libsndfile1 libsnmp-base libsnmp40 libsoup2.4-common libsqlite3-0 libss2 libssl3 libsynctex2 libsysmetrics1 libtasn1-6 libtiff5 libtinfo6 libtss2-esys-3.0.2-0 libtss2-mu0 libtss2-sys1 libtss2-tcti-cmd0 libtss2-tcti-device0 libtss2-tcti-mssim0 libtss2-tcti-swtpm0 libudev1 libuno-cppuhelpergcc3-3 libuno-purpenvhelpergcc3-3 libuno-sal3 libuno-salhelpergcc3-3 libuuid1 libuv1 libvpx7 libwayland-client0 libwayland-cursor0 libwayland-egl1 libwayland-server0 libwbclient0 libwebp7 libwebpdemux2 libwebpmux3 libx11-6 libx11-data libx11-xcb1 libxml2 libxpm4 libxslt1.1 libyajl2 linux-firmware linux-generic-hwe-22.04 linux-headers-generic-hwe-22.04 linux-image-generic-hwe-22.04 linux-libc-dev linux-tools-common locales login logrotate logsave nano nautilus nautilus-data ncurses-base netplan.io networkd-dispatcher ntfs-3g openssl openvpn orca passwd poppler-utils printer-driver-foo2zjs printer-driver-foo2zjs-common procps python3 python3-cryptography python3-future python3-gdbm python3-idna python3-jwt python3-ldb python3-lib2to3 python3-mako python3-minimal python3-oauthlib python3-paramiko python3-pil python3-pkg-resources python3-problem-report python3-protobuf python3-renderpm python3-reportlab python3-reportlab-accel python3-urllib3 python3.10 python3.10-minimal rfkill rsync rsyslog samba-libs snapd sudo tar thunderbird thunderbird-gnome-support thunderbird-locale-en tracker-extract tracker-miner-fs tzdata ubuntu-advantage-desktop-daemon ubuntu-drivers-common ubuntu-report udev uno-libs-private ure util-linux vim-common vim-tiny wireless-regdb wpasupplicant xserver-common xserver-xephyr xserver-xorg-core xserver-xorg-legacy xwayland xxd zlib1g
2025-02-28 18:57:05,777 INFO Writing dpkg log to /var/log/unattended-upgrades/unattended-upgrades-dpkg.log
^C
san@UbuDesk:~/docker_compose_workshop$ ps aux | grep unattended-upgrades
root         659  0.0  0.4 121012 23424 ?        Ssl  18:52   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
san        64235 14.0  0.0  12100  2816 pts/0    S+   19:26   0:00 grep --color=auto unattended-upgrades
san@UbuDesk:~/docker_compose_workshop$ ls /var/lib/dpkg/lock-frontend
/var/lib/dpkg/lock-frontend
san@UbuDesk:~/docker_compose_workshop$ ls /var/lib/dpkg/lock-frontend
/var/lib/dpkg/lock-frontend
san@UbuDesk:~/docker_compose_workshop$ sudo lsof /var/lib/dpkg/lock-frontend
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1000/gvfs
      Output information may be incomplete.
lsof: WARNING: can't stat() fuse.portal file system /run/user/1000/doc
      Output information may be incomplete.
COMMAND    PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
unattende 2210 root   10uW  REG    8,3        0 817293 /var/lib/dpkg/lock-frontend
san@UbuDesk:~/docker_compose_workshop$ sudo systemctl stop unattended-upgrades
san@UbuDesk:~/docker_compose_workshop$ sudo kill -9 $(pgrep unattended-upgrades)

Usage:
 kill [options] <pid> [...]

Options:
 <pid> [...]            send signal to every <pid> listed
 -<signal>, -s, --signal <signal>
                        specify the <signal> to be sent
 -q, --queue <value>    integer value to be sent with the signal
 -l, --list=[<signal>]  list all signal names, or convert one to a name
 -L, --table            list all signal names in a nice table

 -h, --help     display this help and exit
 -V, --version  output version information and exit

For more details see kill(1).
san@UbuDesk:~/docker_compose_workshop$ sudo rm -f /var/lib/dpkg/lock-frontend
sudo rm -f /var/lib/dpkg/lock
sudo rm -f /var/lib/apt/lists/lock
san@UbuDesk:~/docker_compose_workshop$ sudo apt update
Hit:1 https://download.docker.com/linux/ubuntu jammy InRelease
Hit:2 http://us.archive.ubuntu.com/ubuntu jammy InRelease
Hit:3 http://security.ubuntu.com/ubuntu jammy-security InRelease
Hit:4 http://us.archive.ubuntu.com/ubuntu jammy-updates InRelease
Hit:5 http://us.archive.ubuntu.com/ubuntu jammy-backports InRelease
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
329 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: https://download.docker.com/linux/ubuntu/dists/jammy/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
san@UbuDesk:~/docker_compose_workshop$ sudo apt install docker-compose
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libreoffice-ogltrans systemd-hwe-hwdb
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  docker-ce docker-ce-cli python3-attr python3-distutils python3-docker
  python3-dockerpty python3-docopt python3-dotenv python3-jsonschema
  python3-lib2to3 python3-pyrsistent python3-setuptools python3-texttable
  python3-websocket
Suggested packages:
  cgroupfs-mount | cgroup-lite python-attr-doc python-jsonschema-doc
  python-setuptools-doc
Recommended packages:
  docker.io
The following NEW packages will be installed:
  docker-compose python3-attr python3-distutils python3-docker
  python3-dockerpty python3-docopt python3-dotenv python3-jsonschema
  python3-pyrsistent python3-setuptools python3-texttable
  python3-websocket
The following packages will be upgraded:
  docker-ce docker-ce-cli python3-lib2to3
3 upgraded, 12 newly installed, 0 to remove and 326 not upgraded.
Need to get 35,8 MB/35,9 MB of archives.
After this operation, 20,2 MB disk space will be freed.
Do you want to continue? [Y/n] Y
Get:1 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce-cli amd64 5:28.0.1-1~ubuntu.22.04~jammy [15,7 MB]
Get:2 http://us.archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-distutils all 3.10.8-1~22.04 [139 kB]
Get:3 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-websocket all 1.2.3-1 [34,7 kB]
Get:4 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-docker all 5.0.3-1 [89,3 kB]
Get:5 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-dockerpty all 0.4.1-2 [11,1 kB]
Get:6 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-docopt all 0.6.2-4 [26,9 kB]
Get:7 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-dotenv all 0.19.2-1 [20,5 kB]
Get:8 http://us.archive.ubuntu.com/ubuntu jammy/main amd64 python3-attr all 21.2.0-1 [44,0 kB]
Get:9 http://us.archive.ubuntu.com/ubuntu jammy-updates/main amd64 python3-setuptools all 59.6.0-1.2ubuntu0.22.04.2 [340 kB]
Get:10 http://us.archive.ubuntu.com/ubuntu jammy/main amd64 python3-pyrsistent amd64 0.18.1-1build1 [55,5 kB]
Get:11 http://us.archive.ubuntu.com/ubuntu jammy/main amd64 python3-jsonschema all 3.2.0-0ubuntu2 [43,1 kB]
Get:12 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 python3-texttable all 1.6.4-1 [11,4 kB]
Get:13 http://us.archive.ubuntu.com/ubuntu jammy/universe amd64 docker-compose all 1.29.2-1 [95,8 kB]
Get:14 https://download.docker.com/linux/ubuntu jammy/stable amd64 docker-ce amd64 5:28.0.1-1~ubuntu.22.04~jammy [19,1 MB]
Fetched 35,8 MB in 17s (2.134 kB/s)
(Reading database ... 208029 files and directories currently installed.)
Preparing to unpack .../00-docker-ce-cli_5%3a28.0.1-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-ce-cli (5:28.0.1-1~ubuntu.22.04~jammy) over (5:27.5.1-1~ubuntu.22.04~jammy) ...
Preparing to unpack .../01-docker-ce_5%3a28.0.1-1~ubuntu.22.04~jammy_amd64.deb ...
Unpacking docker-ce (5:28.0.1-1~ubuntu.22.04~jammy) over (5:27.5.1-1~ubuntu.22.04~jammy) ...
Preparing to unpack .../02-python3-lib2to3_3.10.8-1~22.04_all.deb ...
Unpacking python3-lib2to3 (3.10.8-1~22.04) over (3.10.4-0ubuntu1) ...
Selecting previously unselected package python3-distutils.
Preparing to unpack .../03-python3-distutils_3.10.8-1~22.04_all.deb ...
Unpacking python3-distutils (3.10.8-1~22.04) ...
Selecting previously unselected package python3-websocket.
Preparing to unpack .../04-python3-websocket_1.2.3-1_all.deb ...
Unpacking python3-websocket (1.2.3-1) ...
Selecting previously unselected package python3-docker.
Preparing to unpack .../05-python3-docker_5.0.3-1_all.deb ...
Unpacking python3-docker (5.0.3-1) ...
Selecting previously unselected package python3-dockerpty.
Preparing to unpack .../06-python3-dockerpty_0.4.1-2_all.deb ...
Unpacking python3-dockerpty (0.4.1-2) ...
Selecting previously unselected package python3-docopt.
Preparing to unpack .../07-python3-docopt_0.6.2-4_all.deb ...
Unpacking python3-docopt (0.6.2-4) ...
Selecting previously unselected package python3-dotenv.
Preparing to unpack .../08-python3-dotenv_0.19.2-1_all.deb ...
Unpacking python3-dotenv (0.19.2-1) ...
Selecting previously unselected package python3-attr.
Preparing to unpack .../09-python3-attr_21.2.0-1_all.deb ...
Unpacking python3-attr (21.2.0-1) ...
Selecting previously unselected package python3-setuptools.
Preparing to unpack .../10-python3-setuptools_59.6.0-1.2ubuntu0.22.04.2_all.deb ...
Unpacking python3-setuptools (59.6.0-1.2ubuntu0.22.04.2) ...
Selecting previously unselected package python3-pyrsistent:amd64.
Preparing to unpack .../11-python3-pyrsistent_0.18.1-1build1_amd64.deb ...
Unpacking python3-pyrsistent:amd64 (0.18.1-1build1) ...
Selecting previously unselected package python3-jsonschema.
Preparing to unpack .../12-python3-jsonschema_3.2.0-0ubuntu2_all.deb ...
Unpacking python3-jsonschema (3.2.0-0ubuntu2) ...
Selecting previously unselected package python3-texttable.
Preparing to unpack .../13-python3-texttable_1.6.4-1_all.deb ...
Unpacking python3-texttable (1.6.4-1) ...
Selecting previously unselected package docker-compose.
Preparing to unpack .../14-docker-compose_1.29.2-1_all.deb ...
Unpacking docker-compose (1.29.2-1) ...
Setting up python3-dotenv (0.19.2-1) ...
Setting up python3-attr (21.2.0-1) ...
Setting up python3-texttable (1.6.4-1) ...
Setting up python3-docopt (0.6.2-4) ...
Setting up docker-ce-cli (5:28.0.1-1~ubuntu.22.04~jammy) ...
Setting up python3-pyrsistent:amd64 (0.18.1-1build1) ...
Setting up python3-lib2to3 (3.10.8-1~22.04) ...
Setting up python3-websocket (1.2.3-1) ...
Setting up python3-dockerpty (0.4.1-2) ...
Setting up python3-distutils (3.10.8-1~22.04) ...
Setting up python3-setuptools (59.6.0-1.2ubuntu0.22.04.2) ...
Setting up python3-docker (5.0.3-1) ...
Setting up python3-jsonschema (3.2.0-0ubuntu2) ...
Setting up docker-ce (5:28.0.1-1~ubuntu.22.04~jammy) ...
Setting up docker-compose (1.29.2-1) ...
Processing triggers for man-db (2.10.2-1) ...
san@UbuDesk:~/docker_compose_workshop$ docker-compose up -d
Creating network "docker_compose_workshop_app-network" with driver "bridge"
Creating volume "docker_compose_workshop_postgres_data" with default driver
Pulling db (postgres:13)...
13: Pulling from library/postgres
7cf63256a31a: Already exists
d1c43e9ce014: Pull complete                                                 8a0f7e55dad9: Pull complete                                                 0340d07b90bb: Pull complete                                                 08ab1447992d: Pull complete                                                 9aeadb38b854: Pull complete                                                 671ab2865cd4: Pull complete                                                 bad67c5d745a: Pull complete                                                 6025eb076e22: Pull complete                                                 8e1cb4da2a59: Pull complete                                                 7c2895b4f604: Pull complete                                                 499d1d4eb3d9: Pull complete                                                 23a9a1509748: Pull complete                                                 44b41f56969e: Pull complete                                                 Digest: sha256:43226c2fa6bac24f8d6e90c99e8cfc44959d4b1dde39fd715835a8250a6204b7
Status: Downloaded newer image for postgres:13
Building api
[+] Building 18.8s (10/10) FINISHED                          docker:default
 => [internal] load build definition from Dockerfile                   0.1s
 => => transferring dockerfile: 199B                                   0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim     0.9s
 => [internal] load .dockerignore                                      0.1s
 => => transferring context: 2B                                        0.0s
 => [1/5] FROM docker.io/library/python:3.9-slim@sha256:d1fd807555208  0.0s
 => [internal] load build context                                      0.0s
 => => transferring context: 6.64kB                                    0.0s
 => CACHED [2/5] WORKDIR /app                                          0.0s
 => [3/5] COPY requirements.txt .                                      0.6s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt          16.0s
 => [5/5] COPY . .                                                     0.3s
 => exporting to image                                                 0.5s
 => => exporting layers                                                0.5s
 => => writing image sha256:b9728788b3729eeb0105e476482b8f3f1de5b2514  0.0s
 => => naming to docker.io/library/docker_compose_workshop_api         0.0s
WARNING: Image for service api was built because it did not already exist. To rebuild this image you must use `docker-compose build` or `docker-compose up --build`.
Pulling pgadmin (dpage/pgadmin4:)...
latest: Pulling from dpage/pgadmin4
f18232174bc9: Pull complete                                                 baf15215d437: Pull complete                                                 10310706b407: Pull complete                                                 ff532a74538f: Pull complete                                                 b3609372ed79: Pull complete                                                 7ac647b180d0: Pull complete                                                 09b82c77e4b0: Pull complete                                                 bc9f31d99706: Pull complete                                                 f0fb1842f0c3: Pull complete                                                 2dc7afb132e7: Pull complete                                                 380cf8e4f913: Pull complete                                                 236726433656: Pull complete                                                 0695f25b9342: Pull complete                                                 b74202090be6: Pull complete                                                 669ceba5e652: Pull complete                                                 6b5b0437a91d: Pull complete                                                 Digest: sha256:bdebdfc4b165c10d0ad60e58f1d7ef41af6c881c9556ae331adaa35bba6dacf3
Status: Downloaded newer image for dpage/pgadmin4:latest
Creating docker_compose_workshop_db_1 ... done
Creating docker_compose_workshop_pgadmin_1 ... done
Creating docker_compose_workshop_api_1     ... done
san@UbuDesk:~/docker_compose_workshop$ docker-compose logs
Attaching to docker_compose_workshop_api_1, docker_compose_workshop_pgadmin_1, docker_compose_workshop_db_1
api_1      | 2025-03-01 00:40:20,638 - __main__ - INFO - Connecting to database: postgresql://postgres:postgres@db:5432/studentsdb
api_1      | 2025-03-01 00:40:20,645 - __main__ - INFO - Attempt 1/30 to connect to the database...
api_1      | 2025-03-01 00:40:21,954 - __main__ - WARNING - Retry connecting to the database (1/30)...
api_1      | 2025-03-01 00:40:21,954 - __main__ - INFO - Attempt 2/30 to connect to the database...
api_1      | 2025-03-01 00:40:22,968 - __main__ - WARNING - Retry connecting to the database (2/30)...
api_1      | 2025-03-01 00:40:22,969 - __main__ - INFO - Attempt 3/30 to connect to the database...
api_1      | 2025-03-01 00:40:23,975 - __main__ - WARNING - Retry connecting to the database (3/30)...
api_1      | 2025-03-01 00:40:23,980 - __main__ - INFO - Attempt 4/30 to connect to the database...
api_1      | 2025-03-01 00:40:24,038 - __main__ - INFO - Successfully connected to the database!
api_1      | /app/app.py:38: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
api_1      |   Base = declarative_base()
api_1      | 2025-03-01 00:40:24,043 - __main__ - INFO - Creating database tables if they don't exist...
api_1      |  * Serving Flask app 'app'
api_1      |  * Debug mode: on
api_1      | 2025-03-01 00:40:24,085 - __main__ - INFO - Database tables created or already exist
api_1      | 2025-03-01 00:40:24,088 - __main__ - INFO - Starting Flask application...
api_1      | 2025-03-01 00:40:24,212 - werkzeug - INFO - WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
api_1      |  * Running on all addresses (0.0.0.0)
api_1      |  * Running on http://127.0.0.1:5000
api_1      |  * Running on http://172.18.0.3:5000
api_1      | 2025-03-01 00:40:24,212 - werkzeug - INFO - Press CTRL+C to quit
api_1      | 2025-03-01 00:40:24,215 - werkzeug - INFO -  * Restarting with stat
api_1      | 2025-03-01 00:40:27,499 - __main__ - INFO - Connecting to database: postgresql://postgres:postgres@db:5432/studentsdb
api_1      | 2025-03-01 00:40:27,500 - __main__ - INFO - Attempt 1/30 to connect to the database...
api_1      | 2025-03-01 00:40:27,817 - __main__ - INFO - Successfully connected to the database!
api_1      | /app/app.py:38: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
api_1      |   Base = declarative_base()
api_1      | 2025-03-01 00:40:27,827 - __main__ - INFO - Creating database tables if they don't exist...
api_1      | 2025-03-01 00:40:27,855 - __main__ - INFO - Database tables created or already exist
api_1      | 2025-03-01 00:40:27,859 - __main__ - INFO - Starting Flask application...
api_1      | 2025-03-01 00:40:27,887 - werkzeug - WARNING -  * Debugger is active!
api_1      | 2025-03-01 00:40:27,891 - werkzeug - INFO -  * Debugger PIN: 858-808-569
db_1       | The files belonging to this database system will be owned by user "postgres".
db_1       | This user must also own the server process.
db_1       |
db_1       | The database cluster will be initialized with locale "en_US.utf8".
db_1       | The default database encoding has accordingly been set to "UTF8".
db_1       | The default text search configuration will be set to "english".
db_1       |
db_1       | Data page checksums are disabled.
db_1       |
db_1       | fixing permissions on existing directory /var/lib/postgresql/data ... ok
db_1       | creating subdirectories ... ok
db_1       | selecting dynamic shared memory implementation ... posix
db_1       | selecting default max_connections ... 100
db_1       | selecting default shared_buffers ... 128MB
db_1       | selecting default time zone ... Etc/UTC
db_1       | creating configuration files ... ok
db_1       | running bootstrap script ... ok
db_1       | performing post-bootstrap initialization ... ok
db_1       | syncing data to disk ... ok
db_1       |
db_1       |
db_1       | Success. You can now start the database server using:
db_1       |
db_1       |     pg_ctl -D /var/lib/postgresql/data -l logfile start
db_1       |
db_1       | initdb: warning: enabling "trust" authentication for local connections
db_1       | You can change this by editing pg_hba.conf or using the option -A, or
db_1       | --auth-local and --auth-host, the next time you run initdb.
db_1       | waiting for server to start....2025-03-01 00:40:22.273 UTC [47] LOG:  starting PostgreSQL 13.20 (Debian 13.20-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
db_1       | 2025-03-01 00:40:22.278 UTC [47] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1       | 2025-03-01 00:40:22.293 UTC [48] LOG:  database system was shut down at 2025-03-01 00:40:20 UTC
db_1       | 2025-03-01 00:40:22.301 UTC [47] LOG:  database system is ready to accept connections
db_1       |  done
db_1       | server started
db_1       | CREATE DATABASE
db_1       |
db_1       |
db_1       | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
db_1       |
db_1       | 2025-03-01 00:40:23.070 UTC [47] LOG:  received fast shutdown request
db_1       | waiting for server to shut down....2025-03-01 00:40:23.074 UTC [47] LOG:  aborting any active transactions
db_1       | 2025-03-01 00:40:23.076 UTC [47] LOG:  background worker "logical replication launcher" (PID 54) exited with exit code 1
db_1       | 2025-03-01 00:40:23.079 UTC [49] LOG:  shutting down
db_1       | 2025-03-01 00:40:23.125 UTC [47] LOG:  database system is shut down
db_1       |  done
db_1       | server stopped
db_1       |
db_1       | PostgreSQL init process complete; ready for start up.
db_1       |
db_1       | 2025-03-01 00:40:23.216 UTC [1] LOG:  starting PostgreSQL 13.20 (Debian 13.20-1.pgdg120+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
db_1       | 2025-03-01 00:40:23.217 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1       | 2025-03-01 00:40:23.217 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1       | 2025-03-01 00:40:23.225 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1       | 2025-03-01 00:40:23.246 UTC [62] LOG:  database system was shut down at 2025-03-01 00:40:23 UTC
db_1       | 2025-03-01 00:40:23.294 UTC [1] LOG:  database system is ready to accept connections
pgadmin_1  | email config is {'CHECK_EMAIL_DELIVERABILITY': False, 'ALLOW_SPECIAL_EMAIL_DOMAINS': [], 'GLOBALLY_DELIVERABLE': True}
pgadmin_1  | NOTE: Configuring authentication for SERVER mode.
pgadmin_1  |
pgadmin_1  | pgAdmin 4 - Application Initialisation
pgadmin_1  | ======================================
pgadmin_1  |
pgadmin_1  | postfix/postlog: starting the Postfix mail system
pgadmin_1  | [2025-03-01 00:40:52 +0000] [1] [INFO] Starting gunicorn 22.0.0
pgadmin_1  | [2025-03-01 00:40:52 +0000] [1] [INFO] Listening at: http://[::]:80 (1)
pgadmin_1  | [2025-03-01 00:40:52 +0000] [1] [INFO] Using worker: gthread
pgadmin_1  | [2025-03-01 00:40:52 +0000] [118] [INFO] Booting worker with pid: 118
san@UbuDesk:~/docker_compose_workshop$ docker-compose ps
        Name                   Command          State          Ports
----------------------------------------------------------------------------
docker_compose_worksh   python app.py           Up      0.0.0.0:5000-
op_api_1                                                >5000/tcp,:::5000-
                                                        >5000/tcp
docker_compose_worksh   docker-entrypoint.sh    Up      0.0.0.0:5432-
op_db_1                 postgres                        >5432/tcp,:::5432-
                                                        >5432/tcp
docker_compose_worksh   /entrypoint.sh          Up      443/tcp, 0.0.0.0:505
op_pgadmin_1                                            0->80/tcp,:::5050-
                                                        >80/tcp
san@UbuDesk:~/docker_compose_workshop$ curl http://localhost:5000/students
[]
san@UbuDesk:~/docker_compose_workshop$curl -X POST http://localhost:5000/students \\
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan Perez", "edad": 21, "carrera": "Ingeniería"}'
{
  "carrera": "Ingenier\u00eda",
  "edad": 21,
  "id": 1,
  "nombre": "Juan Perez"
}
san@UbuDesk:~/docker_compose_workshop$ curl http://localhost:5000/students
[
  {
    "carrera": "Ingenier\u00eda",
    "edad": 21,
    "id": 1,
    "nombre": "Juan Perez"
  }
]
san@UbuDesk:~/docker_compose_workshop$ curl -X PUT http://localhost:5000/stu
dents/1 \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Juan Perez Actualizado", "edad": 22}'
{
  "carrera": "Ingenier\u00eda",
  "edad": 22,
  "id": 1,
  "nombre": "Juan Perez Actualizado"
}
san@UbuDesk:~/docker_compose_workshop$ curl -X DELETE http://localhost:5000/students/1
{
  "message": "Student 1 deleted successfully"
}
san@UbuDesk:~/docker_compose_workshop$ curl http://localhost:5000/students
[]
san@UbuDesk:~/docker_compose_workshop$ git init

```
