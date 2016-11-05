
#今天新学的内容8.23
- 提交改变 commit
- 分支Branches记录多种不同想法
- 分支合并 Merged

- 修改 1.在线修改
        直接在网页点击文件→编辑完成后edit→滚到页面底部→点击commit change按钮确认提交
       2.本地修改（把项目克隆到本地后再改）
        打卡客户端→右上角+号，切换到clone→找到文件夹后点击clone repository→从本地找到克隆的文件夹→打开→编辑并保存→切换github应用窗口→changes列出改变
        →点击commit&sync按钮同步（ps有点不清楚...）
    
-申请合并（暂时不学）
-同步  直接在github编辑本地网络同时同步
       本地同步 在网页界面按upload files 拖本地文件进去
         
*1）新建Text文件夹作为仓库根目录（文件夹名字随意命名）

*2）将需要上传的代码文件加入到Text根目录

*3）在根目录下建立仓库
使用命令行或Git Bash，输入下面命令：先进入到Text根目录下，再输入git init（初始化一个仓库）

*4）将所有文件添加到仓库
使用命令行或Git Bash，输入下面命令：git add .

*5）提交
使用命令行或Git Bash，输入下面命令：git commit -m “CommitInfo”

*6）添加源到GitHub
git remote add origin git@github.com:YourName/YourRepositroy.git

*7）上传源到GitHub
git push -u origin master
        