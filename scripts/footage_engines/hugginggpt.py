import torch
from diffusers import DiffusionPipeline
from diffusers.utils import export_to_video

pipe = DiffusionPipeline.from_pretrained("damo-vilab/text-to-video-ms-1.7b", torch_dtype=torch.float16, variant="fp16")
pipe = pipe.to("cuda")

def upload(video_path):
	# TODO: implement
	video_url = "123"
	return video_url

def generate(prompt, footage_options):
	# TODO: use footage_options to configure the video, i.e. num_frames
	video_frames = pipe(prompt, num_frames=128).frames
	video_path = export_to_video(video_frames)
	print("video_path:", video_path)
	video_url = upload(video_path)
	return video_url