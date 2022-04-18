import sys

for i in range( 1, len(sys.argv) ):
    if "-user=" in sys.argv[i]:
        GITHUB_USER = sys.argv[i][6:]
    elif "-token" in sys.argv[i]:
        GITHUB_TOKEN = sys.argv[i][7:]
    elif "-target_dir=" in sys.argv[i]:
        target_dir = sys.argv[i][12:]
