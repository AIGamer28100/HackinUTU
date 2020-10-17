from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from recognition.camera import FaceDetect
# Create your views here.

def index(request):
	return render(request, 'recognition/index.html')

class gen():
	def frame(self):
		self.camera = FaceDetect()
		while self.camera.fps._numFrames < 50:
			self.frame, self.name = self.camera.get_frame()
			self.frame = self.frame.tobytes()
			yield(b'--frame\r\n'
				b'Content_type: image/jpeg\r\n\r\n' + self.frame + b'\r\n\r\n')

def facecam_feed(request):
	x = gen()
	return StreamingHttpResponse(x.frame(),
					content_type='multipart/x-mixed-replace; boundary=frame')
