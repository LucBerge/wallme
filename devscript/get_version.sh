if [[ "$PWD" = */devscript ]]; then
    cd ..
fi

line=$(grep "version=" setup.py)
version=$(echo ${line#*"version='"} | cut -d"'" -f 1)
echo $version
