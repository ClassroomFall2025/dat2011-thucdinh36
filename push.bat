@echo off
echo ==============================
echo    AUTO GIT PUSH TO GITHUB
echo ==============================
git add .
git commit -m "Auto update"
git push origin main
echo ------------------------------
echo  Đã đẩy bài lên GitHub thành công!
pause