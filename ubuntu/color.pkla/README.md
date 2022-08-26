---
title: 색상 프로필을 만들려면 인증이 필요합니다.
description: XRDP 연결시 (색상 프로필을 만들려면 인증이 필요합니다.)라는 메시지가 반복적으로 표시될 경우 해결 방법
---


색상 프로필을 만들려면 인증이 필요합니다.
===


요약
---


### /etc/polkit-1/localauthority/50-local.d 디렉토리 생성


```
$ sudo mkdir -p /etc/polkit-1/localauthority/50-local.d
```


### /etc/polkit-1/localauthority/50-local.d/color.pkla 파일 편집


```
$ sudo vi /etc/polkit-1/localauthority/50-local.d/color.pkla
```


해당 파일에 아래 내용을 작성함.


```
[Allow colord for all users]
Identity=unix-user:*
Action=org.freedesktop.color-manager.create-device;org.freedesktop.color-manager.create-profile;org.freedesktop.color-manager.delete-device;org.freedesktop.color-manager.delete-profile;org.freedesktop.color-manager.modify-device;org.freedesktop.color-manager.modify-profile
ResultAny=yes
ResultInactive=yes
ResultActive=yes
```


혹은 wget으로 해당 파일을 다운로드 받아서 복사해도 됩니다.


```
$ wget https://raw.githubusercontent.com/boyinblue/test/main/ubuntu/color.pkla/color.pkla
$ sudo mv color.pkla /etc/polkit-1/localauthority/50-local.d/
```


이상입니다
