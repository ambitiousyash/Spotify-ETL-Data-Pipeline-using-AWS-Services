{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue255;\red45\green45\blue45;
\red0\green0\blue255;\red101\green76\blue29;\red0\green0\blue109;\red0\green0\blue0;\red144\green1\blue18;
\red19\green118\blue70;\red32\green108\blue135;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c100000;\cssrgb\c23137\c23137\c23137;
\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c0\c0\c0;\cssrgb\c63922\c8235\c8235;
\cssrgb\c3529\c52549\c34510;\cssrgb\c14902\c49804\c60000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  json\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  os\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  boto3\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  spotipy\cb1 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  boto3\cb1 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  datetime \cf2 \strokec2 import\cf4 \strokec4  datetime\cb1 \
\
\cf2 \cb3 \strokec2 from\cf4 \strokec4  spotipy.oauth2 \cf2 \strokec2 import\cf4 \strokec4  SpotifyClientCredentials\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def\cf4 \strokec4  \cf6 \strokec6 lambda_handler\cf4 \strokec4 (\cf7 \strokec7 event\cf4 \strokec4 , \cf7 \strokec7 context\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     \cb1 \
\cb3     client_id \strokec8 =\strokec4  os.environ[\cf9 \strokec9 'client_id'\cf4 \strokec4 ]\cb1 \
\cb3     client_secret \strokec8 =\strokec4  os.environ[\cf9 \strokec9 'client_secret'\cf4 \strokec4 ]\cb1 \
\
\cb3     client_credentials_manager \strokec8 =\strokec4  SpotifyClientCredentials(\cf7 \strokec7 client_id\cf4 \strokec8 =\strokec4 client_id, \cf7 \strokec7 client_secret\cf4 \strokec8 =\strokec4 client_secret)\cb1 \
\cb3     sp \strokec8 =\strokec4  spotipy.Spotify(\cf7 \strokec7 client_credentials_manager\cf4 \strokec8 =\strokec4 client_credentials_manager)\cb1 \
\cb3     playlists \strokec8 =\strokec4  sp.user_playlists(\cf9 \strokec9 'spotify'\cf4 \strokec4 )\cb1 \
\
\cb3     playlist_link \strokec8 =\strokec4  \cf9 \strokec9 "https://open.spotify.com/playlist/7rBjBuIpTiE0UOqHqCtupz"\cf4 \cb1 \strokec4 \
\cb3     playlist_URI \strokec8 =\strokec4  playlist_link.split(\cf9 \strokec9 "/"\cf4 \strokec4 )[\strokec8 -\cf10 \strokec10 1\cf4 \strokec4 ].split(\cf9 \strokec9 "?"\cf4 \strokec4 )[\cf10 \strokec10 0\cf4 \strokec4 ]\cb1 \
\
\cb3     spotify_data \strokec8 =\strokec4  sp.playlist_tracks(playlist_URI)\cb1 \
\
\cb3     client \strokec8 =\strokec4  boto3.client(\cf9 \strokec9 's3'\cf4 \strokec4 )\cb1 \
\cb3     filename \strokec8 =\strokec4  \cf9 \strokec9 "spotify_raw_"\cf4 \strokec4  \strokec8 +\strokec4  \cf11 \strokec11 str\cf4 \strokec4 (datetime.now()) \strokec8 +\strokec4  \cf9 \strokec9 ".json"\cf4 \cb1 \strokec4 \
\cb3     client.put_object(\cb1 \
\cb3         \cf7 \strokec7 Bucket\cf4 \strokec8 =\cf9 \strokec9 "spotify-etl-project-sarthak1"\cf4 \strokec4 ,\cb1 \
\cb3         \cf7 \strokec7 Key\cf4 \strokec8 =\cf9 \strokec9 "raw_data/to_processed/"\cf4 \strokec4  \strokec8 +\strokec4  filename,\cb1 \
\cb3         \cf7 \strokec7 Body\cf4 \strokec8 =\strokec4 json.dumps(spotify_data)\cb1 \
\cb3     )\cb1 \
}