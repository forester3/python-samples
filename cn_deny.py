import urllib.request

ip_adr_list=[  ["cn_ip.list", "https://ipv4.fetus.jp/cn.txt"],
                ["au_ip.list", "https://ipv4.fetus.jp/au.txt"] ]

loaded = []

for [fn, url]  in ip_adr_list:
    print( "loading:", url, "save:", fn )
    urllib.request.urlretrieve(url,"{0}".format(fn))
    loaded.append(fn)

for path in loaded:
    sep = 0
    with open(path) as f:
        line_count = 0
        sep_path = path + str(sep)
        for line in f:
            if line == '\n':
                continue
            elif line[0] == '#':
                continue
            else :
                line = line.strip()
                with open(sep_path, mode='a') as wf:
                    line_count += 1;
                    if( line_count >= 255 ) :
                        ip_out = '"' + line + '\"\n'
                        wf.write( ip_out )
                        print( 'new file !', path )
                        line_count = 0
                        sep += 1
                        sep_path = path + str(sep)
                        continue
                    else :
                        ip_out = '"' + line + '\",\n'
                        wf.write( ip_out )
                        print( ip_out )

