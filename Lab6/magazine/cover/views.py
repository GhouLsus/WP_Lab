from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        # Get form data
        image = request.FILES.get('image')  # Uploaded image
        bg_color = request.POST.get('bg_color', '#FFFFFF')  # Default background color to white
        title = request.POST.get('title', 'Magazine Title')  # Default title text
        subtitle = request.POST.get('subtitle', 'Subtitle')  # Default subtitle text
        title_size = request.POST.get('title_size', '40')  # Default title font size to 40
        subtitle_size = request.POST.get('subtitle_size', '30')  # Default subtitle font size to 30
        title_color = request.POST.get('title_color', '#000000')  # Default title color to black
        subtitle_color = request.POST.get('subtitle_color', '#555555')  # Default subtitle color to gray

        # Ensure title_size and subtitle_size are integers
        try:
            title_size = int(title_size)
        except ValueError:
            title_size = 40  # Fallback to default if invalid value provided

        try:
            subtitle_size = int(subtitle_size)
        except ValueError:
            subtitle_size = 30  # Fallback to default if invalid value provided

        # Print to debug values being passed
        print(f'bg_color: {bg_color}, title_size: {title_size}, subtitle_size: {subtitle_size}')
        
        return render(request, 'cover/front_cover.html', {
            'image': image,
            'bg_color': bg_color,
            'title': title,
            'subtitle': subtitle,
            'title_size': title_size,
            'subtitle_size': subtitle_size,
            'title_color': title_color,
            'subtitle_color': subtitle_color,
        })
    
    return render(request, 'cover/form.html')
