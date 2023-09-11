// JavaScript code to toggle the mobile menu
const menuIcon = document.getElementById('menu-icon');
const navbar = document.getElementById('navbar');

menuIcon.addEventListener('click', () => {
    navbar.classList.toggle('show');
});
// JavaScript code to fetch and display YouTube video subtitles
const videoPlayer = document.querySelector('.video-container iframe');
const subtitlesContainer = document.getElementById('subtitles');

// Replace with your actual YouTube video ID
const videoId = 'VIDEO_ID_HERE';

// Load the YouTube API
function onYouTubeIframeAPIReady() {
    const player = new YT.Player(videoPlayer, {
        videoId: videoId,
        playerVars: {
            cc_lang_pref: 'en' // Specify the language preference (e.g., 'en' for English)
        },
        events: {
            onReady: onPlayerReady
        }
    });
}

// This function is called when the YouTube player is ready
function onPlayerReady(event) {
    const player = event.target;

    // Set up an event listener to monitor the state of the captions
    player.addEventListener('onCaptionStateChange', onCaptionStateChange);

    // Load the video with captions
    player.loadModule('captions');
    player.loadModule('cc');
}

// This function is called when the caption state changes (e.g., captions are loaded)
function onCaptionStateChange(event) {
    const player = event.target;

    if (event.data === 'SHOWING') {
        // Get the current caption text
        const captionText = player.getOption('captions', 'tracklist')[0].activeCues[0].text;

        // Display the caption text in the subtitles container
        subtitlesContainer.innerHTML = captionText;
    } else {
        // Hide the subtitles container if no captions are showing
        subtitlesContainer.innerHTML = '';
    }
}

