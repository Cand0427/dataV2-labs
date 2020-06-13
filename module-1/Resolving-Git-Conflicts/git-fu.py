git
if __name__ == '__main__':
    print("this is the original message")
    git commit -am "adding git-fu file"
    git push
    git checkout -b conflict-branch
    
