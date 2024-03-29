import instaloader

async def instagram(url):
  
  # Function to determine the type of media from the provided URL and download it
  L = instaloader.Instaloader()
      
  # Get the id from the URL
  item_id = url.split("/")[-2]
      
  try:
    # If the URL corresponds to a profile, download the profile picture
    profile = instaloader.Profile.from_username(L.context, item_id)
    L.download_profile(profile_pic_only=True, target="downloads/", filename=filename)
    return filename
  except instaloader.ProfileNotExistsException:
    # If not a profile, then try downloading the post
    try:
      post = instaloader.Post.from_shortcode(L.context, item_id)
      L.download_post(post, target="downloads/", filename=filename)
    except instaloader.ProfileNotExistsException:
      return "Media not found or unsupported type."
