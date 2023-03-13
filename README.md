My devops scripts showing answers to the question
git clone https://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@github.com/ikonbethel/alx-low_level_programming.git
find . -type f | xargs -Ix sed -i.bak -r 's/\r//g' x
git add  . 
[06/01, 14:34] Bethel: git config --global user.name "Ikonbethel"
[06/01, 14:34] Bethel: git config --global user.email "Ikonbethel@gmail.com"
grep -URl $'\r' .
chmod +x ./*
git commit  -m 'making files executable 'rm *.bakgit push
