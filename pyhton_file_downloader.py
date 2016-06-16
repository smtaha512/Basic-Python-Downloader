from urllib import request

def file_downloader(link):
    response = request.urlopen(link)
    file = response.read()
    file = str(file)
    lines = file.split("\\n")
    file_name = 'NewFile.txt'
    downloaded_file = open(file_name, "w")
    for line in lines:
        downloaded_file.write(line)
        downloaded_file.write("\n")
    downloaded_file.close()
    return

def video_file_downloader(link):
    response = request.urlopen(link)
    file = response.read()
    file_name = 'NewFile.mp4'
    downloaded_file = open(file_name, "wb+")
    downloaded_file.write(file)
    downloaded_file.close()
    return

video_file_downloader("https://r3---sn-25ge7nld.googlevideo.com/videoplayback?pl=22&itag=36&upn=xIt5mI427Wo&source=youtube&id=o-AD57DqoATfjJ5Qg5skB0Zbhg7phaB8p65YTV9XR7b8Ev&mn=sn-25ge7nld&mm=31&ip=37.187.92.173&ms=au&sparams=dur,id,initcwndbps,ip,ipbits,itag,lmt,mime,mm,mn,ms,mv,nh,pl,requiressl,source,upn,expire&mv=m&mt=1466042927&signature=2E1E620DD529EAFFA3EC7169DA32B930A0148B78.0C4DCECC307FB7B9D1961AB7883178E68D0652B4&fexp=9405988,9408208,9416126,9416891,9418778,9419451,9422596,9423965,9428398,9431012,9432565,9433096,9433380,9433672,9433780,9433946,9434899,9435264,9435526,9435667,9435876,9436835,9437066,9437553,9437954,9437982,9438036,9438256,9438567&initcwndbps=1618750&requiressl=yes&key=yt6&mime=video/3gpp&nh=IgpwcjAxLnBhcjEwKgkxMjcuMC4wLjE&sver=3&dur=10.216&ipbits=0&expire=1466064680&lmt=1426646159065355&ratebypass=yes&&title=DigitalMedia+10sec+video")
file_downloader("https://wordpress.org/plugins/about/readme.txt")