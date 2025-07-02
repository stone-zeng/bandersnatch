# rm -rf downloads && mkdir downloads
rm -v downloads/status
echo "Running bandersnatch..."
# python -m bandersnatch -c run/bandersnatch.conf mirror
nohup python -u -m bandersnatch -c run/bandersnatch.conf mirror 1> /dev/null 2> run/bandersnatch-$(date "+%Y-%m-%d_%H-%M-%S").log &
