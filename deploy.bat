@echo off
echo ============================
echo 🚀 Atualizando API no GitHub
echo ============================

cd /d C:\Users\Juven\OneDrive\Desktop\Apiml

git add .
git commit -m "Deploy automático"
git push origin main

echo ============================
echo ✅ Deploy enviado para o GitHub
echo (O Render vai atualizar sozinho)
echo ============================
pause
