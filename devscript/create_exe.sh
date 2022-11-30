if [[ "$PWD" = */devscript ]]; then
    cd ..
fi

rm -r dist
echo -e "from wallme.main import main\nmain()" >> wallme.py
pyinstaller --noconfirm --onefile --windowed "wallme.py"
rm  wallme.py wallme.spec
rm -r build
