Note: If you meet any problem when you testing our project, please contact with us without hesitation.

# 环境 Environment
运行前请打开xampp并运行服务器
用conda环境文件(.yaml)直接导入
direct import with conda environment file (.yaml)
# Environment
Open xampp and run the server before running it.
Direct import with conda environment file (.yaml)
direct import with condo environment file (.yaml)

或者 or

pip install bcrypt==4.1.3 blinker==1.8.1 click==8.1.7 colorama==0.4.6 flask==3.0.3 flask-login==0.6.3 flask-mail==0.9.1 flask-sqlalchemy==3.1.1 greenlet==3.0.3 importlib-metadata==7.1.0 itsdangerous==2.2.0 jinja2==3.1.3 markupsafe==2.1.5 pymysql==1.1.0 sqlalchemy==2.0.29 typing-extensions==4.11.0 werkzeug==3.0.2 zipp==3.18.1

然后通过运行 outwork.py 运行项目

# 邮箱设置 Email Configs(我们已经设置好了，如果需要改变，请按以下操作来进行操作/We've set it up, if you need to change it, do the following steps)
app.config['MAIL_SERVER'] = '邮箱服务器地址/email server address' # 比如QQ邮箱：smtp.qq.com
app.config['MAIL_PORT'] = 587 # 465如果你用SSL/465 for SSL
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = '你的邮箱账号/your mail address' 
app.config['MAIL_PASSWORD'] = '你的邮箱密钥，不是密码/your mail token, not password' # QQ邮箱去设置里开启第三方服务查看
app.config['MAIL_DEFAULT_SENDER'] = '你的邮箱账号/your mail address'


# 登录和注册以及导入数据库 Login&Register&Database
注册需要学校邮箱(格式为xxxxx@uic.edu.cn是老师xxxxxxxx@mail.uic.edu.cn是学生)，去收件邮箱然后复制链接到正在运行project的电脑上点链接设置密码完成注册，需要 uic 的邮箱来完成注册 Require uic email to register, needs to click the link in email。（若没有学生邮箱可以直接用数据库现成的 student 属性的邮箱账号拿来测试，密码都是 12345678）数据库中默认的有管理员和学生的，若要测试老师的功能，可以注册一个老师账号或者将数据库里的 admin 的 type 改成老师
数据库名字：llm，在phpmyadmin 创建llm 数据库后导入llm 文件夹下的 llm.sql 如果用自己的账号要使用 admin账户，创建账号之后去数据库或在数据库里手动去改成Admin来测试
# Login&Register Login&Register
Register need school email (格式为xxxxx@uic.edu.cn是老师xxxxxxxx@mail.uic.edu.cn is a student), go to the incoming mailbox and then copy the link to the computer that is running the project and click the link to set the password to complete the registration, need uic's email to complete the registration Require uic email to register, needs to click the link in email. (If there is no student email you can directly use the database ready-made student attribute of the email account to test, the password is 12345678)There are administrators and students in the database by default, if you want to test the teacher's function, you can register a teacher account or change the type of admin in the database to teacher.

Database(schema) name: llm, in phpmyadmin create llm database after importing llm folder under the llm.sql If you use your own account to use the admin account, after creating the account to the database or in the database manually to change to Admin to test


学生部分的某个细节功能的概述和引导
#student addtopic
学生的 addtopic 功能，request 之后直接连接到管理员页面，测试的话可以 request 后切到管理员账号登录处理学生的 request，这点受限于时长以及我们的完成度较高需展示的功能过多，所以没有在 demo 中展示出来，我们在 presentation 的 demo 中展示了这一功能，麻烦老师需要的话按刚才说的步骤进行测试
one of the detailed features of the student section
#student addtopic
The addtopic function for students connects directly to the administrator page after request, so if you want to test it, you can log in to the administrator account after request to handle the request from students. This point is limited by the length of time and the fact that we need to show too many functions for our high degree of completion, so we didn't show it in the demo, but we showed it in the presentation of the We have shown this function in the demo of the presentation, if you need it, please test it according to the steps mentioned just now.




以下是关于老师及管理员部分的部分细节功能概述

# 搜索 search
组合五项输入进行搜索，没有要求的项目可以留空，reset键快速重置输入，按下搜索将展示全部符合要求的assignment questions，点击view variation键查看问题变体，点击view answer键查看LLM回答，点击图片可以放大查看，此界面分数为平均分，点击score detail键查看详细评分以及各评分对应评论。
Combine five inputs to perform a search. You can leave any fields that don't have requirements blank. Use the reset button to quickly clear the inputs. Press the search button to display all assignment questions that meet the criteria. Click the view variation button to see different versions of a question. Click the view answer button to see the LLM's response. Click on the image to enlarge it. This interface shows the average score. Click the score detail button to view detailed scores and the corresponding comments for each score.

#新增问题 add question
从search界面点击add question键进入新增问题页，输入问题信息并上传回答图片，注意课程需要在现有课程中选择一门，点击submit，即可成功提交请求，等待管理员审核通过后，新问题加入数据库，并可以在search界面显示。
From the search interface, click the add question button to enter the add new question page. Enter the question information and upload an image of the answer. Note that you need to select a course from the existing courses. Click submit to successfully submit the request. After the administrator approves it, the new question will be added to the database and will be displayed in the search page.

#上传实验 upload experiment
点击导航栏experiment键进入experiment页面，可以查看目前账号已上传的实验和状态，回到search界面点击需要上传实验的问题upload experiment键，进入上传实验页面，输入实验信息，上传图片，点击submit，即可成功上传实验，回到experiment页面，即可看到新上传的实验，如果未提交，submit request键亮起，点击修改为状态为已提交，等待管理员审核通过，实验作为新variation加入数据库，并可以在search界面显示。
Click the experiment button in the navigation bar to enter the experiment page, where you can view the experiments that have been uploaded by the current account and their statuses. Return to the search interface and click the upload experiment button for the question you need to upload an experiment for. This will take you to the upload experiment page. Enter the experiment information and upload an image, then click submit to successfully upload the experiment. Go back to the experiment page to see the newly uploaded experiment. If it has not been submitted yet, the submit request button will be highlighted. Click it to change the status to submitted and wait for the administrator's approval. Once approved, the experiment will be added to the database as a new variation and will be displayed on the search interface.

#分数调整 update score
在查看详细分数界面，点击update score按钮进入上传分数页面，输入分数和评价，即可提交，等待管理员审核通过，分数加入数据库，search界面对应平均分变化，并可以在详细分数界面查看新分数，注意每个回答单个账号只允许提交一次评分。
In the view detailed scores interface, click the update score button to enter the upload scores page. Enter the score and review, then submit it. Once approved by the administrator, the score will be added to the database, the corresponding average score on the search interface will change, and the new score can be viewed in the detailed scores interface. Note that each account is only allowed to submit a rating for each answer once.

#新增课程 add course
点击导航栏course键进入course页面，可以查看所有的课程，点击add a course键进入新增课程页面，输入课程信息提交，课程类别只能从已有的三种选其一，等待管理员审核通过，课程加入数据库。
Click the course button in the navigation bar to enter the course page, where you can view all the courses. Click the add a course button to go to the add course page, enter the course information, and submit it. The course category can only be selected from the existing three options. Once approved by the administrator, the course will be added to the database.

#请求 request
点击导航栏request键进入request页面，老师账号进入请求页面显示当前账号提交的所有请求，可以查看状态，无法操作，管理员账号进入请求页面显示当前所有的请求，包括已经处理的和没有处理的请求，对于没有处理的请求，handle键亮起，点击进入处理请求页面，可以选择pass或者reject，点击submit提交，将对应请求操作加入数据库
Click the request button in the navigation bar to enter the request page. Teacher accounts will see all the requests submitted by their account, where they can view the status but cannot take any actions. Administrator accounts will see all current requests, including both processed and unprocessed requests. For unprocessed requests, the handle button will be highlighted. Clicking it will take you to the handle request page, where you can choose to pass or reject the request. Click submit to submit the action, and the corresponding request operation will be added to the database.