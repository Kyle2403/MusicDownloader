export PYTHONIOENCODING=UTF-8
in=$1
out=$2
python main.py < $in > $out
echo 'Result'
cat $out