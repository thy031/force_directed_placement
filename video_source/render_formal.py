import sys,subprocess
from playwright.sync_api import sync_playwright
a,b,name=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
ff=subprocess.Popen(['ffmpeg','-v','error','-y','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',f'v4/out/{name}.mp4'],stdin=subprocess.PIPE)
with sync_playwright() as p:
    br=p.chromium.launch();pg=br.new_page(viewport={'width':1920,'height':1080})
    pg.goto('file:///tmp/claude-0/-home-claude/ed5f1e33-3889-5641-93c5-c8e9efc95c84/scratchpad/v4/formal.html');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(500)
    for f in range(a,b):
        pg.evaluate(f'frame({f/30})');ff.stdin.write(pg.screenshot(type='jpeg',quality=93))
    ff.stdin.close();ff.wait();br.close()
print('done',name)
