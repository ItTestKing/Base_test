@echo off
start pytest E:\work\Base_test\test_dir\test_pic.py --html=../report/admin.html --self-contained-html --reuse-session --demo_mode
echo "运行完毕"
exit