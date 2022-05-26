#!/usr/bin/python3

""" 필요한 패키지들 설치 방법 """
""" sudo apt-get install paramiko """
""" sudo apt-get install scp """

import sys

def upload_file(host, id, pw, local_path, remote_path):
  import paramiko
  from scp import SCPClient, SCPException

  ssh_client = paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh_client.connect(host, username=id, password=pw)

  try:
    with SCPClient(ssh_client.get_transport()) as scp:
      scp.put(local_path, remote_path, preserve_times=True)
  except SCPException:
    print("SCP 업로드에 실패하였습니다.")
    print("Remote Path :", remote_path)
    url = ''
  print("SCP 업로드에 성공하였습니다.")

  ssh_client.close()

def main():
  host = None
  id = None
  pw = None
  local = None
  remote = None

  for i in range(1,len(sys.argv)):
    if "-host=" in sys.argv[i]:
      host = sys.argv[i][6]
    elif "-id=" in sys.argv[i]:
      id = sys.argv[i][4:]
    elif "-pw=" in sys.argv[i]:
      pw = sys.argv[i][4:]
    elif "-local=" in sys.argv[i]:
      local_path = sys.argv[i][7:]
    elif "-remote=" in sys.argv[i]:
      remote_path = sys.argv[i][8:]

  if not host:
    host = input("hostname :")
  if not id:
    id = input("id :")
  if not pw:
    pw = input("pw :")
  if not local:
    local_path = input("local filename :")
  if not remote:
    remote_path = input("remote path :")

  print("host :", host)
  print("id :", id)
  print("pw :", pw)
  print("local_path :", local_path)
  print("remote_path :", remote_path)

  upload_file( host, id, pw, local_path, remote_path )

if __name__ == '__main__':
  main()
