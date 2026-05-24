{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red157\green0\blue210;\red255\green255\blue255;\red45\green45\blue45;
\red0\green0\blue255;\red101\green76\blue29;\red0\green0\blue109;\red0\green0\blue0;\red144\green1\blue18;
\red32\green108\blue135;\red19\green118\blue70;\red15\green112\blue1;}
{\*\expandedcolortbl;;\cssrgb\c68627\c0\c85882;\cssrgb\c100000\c100000\c100000;\cssrgb\c23137\c23137\c23137;
\cssrgb\c0\c0\c100000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c0\c0\c0;\cssrgb\c63922\c8235\c8235;
\cssrgb\c14902\c49804\c60000;\cssrgb\c3529\c52549\c34510;\cssrgb\c0\c50196\c0;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \cb3 \expnd0\expndtw0\kerning0
import\cf4  json\cb1 \
\cf2 \cb3 import\cf4  boto3\cb1 \
\cf2 \cb3 from\cf4  datetime \cf2 import\cf4  datetime\cb1 \
\cf2 \cb3 from\cf4  io \cf2 import\cf4  StringIO\cb1 \
\cf2 \cb3 import\cf4  pandas \cf2 as\cf4  pd\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 def\cf4  \cf6 album\cf4 (\cf7 data\cf4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     album_list = []\cb1 \
\cb3     \cf2 for\cf4  row \cf2 in\cf4  data[\cf9 'items'\cf4 ]:\cb1 \
\cb3         \cf2 try\cf4 :\cb1 \
\cb3             album = row[\cf9 'track'\cf4 ][\cf9 'album'\cf4 ]\cb1 \
\cb3             album_id = album.get(\cf9 'id'\cf4 )\cb1 \
\cb3             album_name = album.get(\cf9 'name'\cf4 )\cb1 \
\cb3             album_release_date = album.get(\cf9 'release_date'\cf4 )\cb1 \
\cb3             album_total_tracks = album.get(\cf9 'total_tracks'\cf4 )\cb1 \
\cb3             album_url = album.get(\cf9 'external_urls'\cf4 , \{\}).get(\cf9 'spotify'\cf4 )\cb1 \
\
\cb3             album_element = \{\cb1 \
\cb3                 \cf9 'album_id'\cf4 : album_id,\cb1 \
\cb3                 \cf9 'name'\cf4 : album_name,\cb1 \
\cb3                 \cf9 'release_date'\cf4 : album_release_date,\cb1 \
\cb3                 \cf9 'total_tracks'\cf4 : album_total_tracks,\cb1 \
\cb3                 \cf9 'url'\cf4 : album_url\cb1 \
\cb3             \}\cb1 \
\cb3             album_list.append(album_element)\cb1 \
\cb3         \cf2 except\cf4  \cf10 Exception\cf4  \cf2 as\cf4  e:\cb1 \
\cb3             \cf6 print\cf4 (\cf5 f\cf9 "Skipping album row due to error: \cf5 \{\cf4 e\cf5 \}\cf9 "\cf4 )\cb1 \
\cb3     \cf2 return\cf4  album_list\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 def\cf4  \cf6 artist\cf4 (\cf7 data\cf4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     artist_list = []\cb1 \
\cb3     \cf2 for\cf4  row \cf2 in\cf4  data[\cf9 'items'\cf4 ]:\cb1 \
\cb3         \cf2 try\cf4 :\cb1 \
\cb3             \cf2 for\cf4  artist \cf2 in\cf4  row[\cf9 'track'\cf4 ][\cf9 'artists'\cf4 ]:\cb1 \
\cb3                 artist_dict = \{\cb1 \
\cb3                     \cf9 'artist_id'\cf4 : artist[\cf9 'id'\cf4 ],\cb1 \
\cb3                     \cf9 'artist_name'\cf4 : artist[\cf9 'name'\cf4 ],\cb1 \
\cb3                     \cf9 'external_url'\cf4 : artist[\cf9 'href'\cf4 ]\cb1 \
\cb3                 \}\cb1 \
\cb3                 artist_list.append(artist_dict)\cb1 \
\cb3         \cf2 except\cf4  \cf10 Exception\cf4  \cf2 as\cf4  e:\cb1 \
\cb3             \cf6 print\cf4 (\cf5 f\cf9 "Skipping artist row due to error: \cf5 \{\cf4 e\cf5 \}\cf9 "\cf4 )\cb1 \
\cb3     \cf2 return\cf4  artist_list\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 def\cf4  \cf6 song\cf4 (\cf7 data\cf4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     song_list = []\cb1 \
\cb3     \cf2 for\cf4  row \cf2 in\cf4  data[\cf9 'items'\cf4 ]:\cb1 \
\cb3         \cf2 try\cf4 :\cb1 \
\cb3             song_id = row[\cf9 'track'\cf4 ][\cf9 'id'\cf4 ]\cb1 \
\cb3             song_name = row[\cf9 'track'\cf4 ][\cf9 'name'\cf4 ]\cb1 \
\cb3             song_duration = row[\cf9 'track'\cf4 ][\cf9 'duration_ms'\cf4 ]\cb1 \
\cb3             song_url = row[\cf9 'track'\cf4 ][\cf9 'external_urls'\cf4 ][\cf9 'spotify'\cf4 ]\cb1 \
\cb3             song_popularity = row[\cf9 'track'\cf4 ][\cf9 'popularity'\cf4 ]\cb1 \
\cb3             song_added = row[\cf9 'added_at'\cf4 ]\cb1 \
\cb3             album_id = row[\cf9 'track'\cf4 ][\cf9 'album'\cf4 ][\cf9 'id'\cf4 ]\cb1 \
\cb3             artist_id = row[\cf9 'track'\cf4 ][\cf9 'album'\cf4 ][\cf9 'artists'\cf4 ][\cf11 0\cf4 ][\cf9 'id'\cf4 ]\cb1 \
\
\cb3             song_list.append(\{\cb1 \
\cb3                 \cf9 'song_id'\cf4 : song_id,\cb1 \
\cb3                 \cf9 'song_name'\cf4 : song_name,\cb1 \
\cb3                 \cf9 'duration_ms'\cf4 : song_duration,\cb1 \
\cb3                 \cf9 'url'\cf4 : song_url,\cb1 \
\cb3                 \cf9 'popularity'\cf4 : song_popularity,\cb1 \
\cb3                 \cf9 'song_added'\cf4 : song_added,\cb1 \
\cb3                 \cf9 'album_id'\cf4 : album_id,\cb1 \
\cb3                 \cf9 'artist_id'\cf4 : artist_id\cb1 \
\cb3             \})\cb1 \
\cb3         \cf2 except\cf4  \cf10 Exception\cf4  \cf2 as\cf4  e:\cb1 \
\cb3             \cf6 print\cf4 (\cf5 f\cf9 "Skipping song row due to error: \cf5 \{\cf4 e\cf5 \}\cf9 "\cf4 )\cb1 \
\cb3     \cf2 return\cf4  song_list\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 def\cf4  \cf6 lambda_handler\cf4 (\cf7 event\cf4 , \cf7 context\cf4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3     s3 = boto3.client(\cf9 's3'\cf4 )\cb1 \
\cb3     s3_resource = boto3.resource(\cf9 's3'\cf4 )\cb1 \
\cb3     Bucket = \cf9 'spotify-etl-project-sarthak1'\cf4 \cb1 \
\cb3     Prefix = \cf9 'raw_data/to_processed/'\cf4 \cb1 \
\
\cb3     spotify_data = []\cb1 \
\cb3     spotify_keys = []\cb1 \
\
\cb3     \cf12 # Get all JSON files from to_processed/\cf4 \cb1 \
\cb3     response = s3.list_objects_v2(\cf7 Bucket\cf4 =Bucket, \cf7 Prefix\cf4 =Prefix)\cb1 \
\cb3     \cf2 if\cf4  \cf9 'Contents'\cf4  \cf5 in\cf4  response:\cb1 \
\cb3         \cf2 for\cf4  file \cf2 in\cf4  response[\cf9 'Contents'\cf4 ]:\cb1 \
\cb3             file_key = file[\cf9 'Key'\cf4 ]\cb1 \
\cb3             \cf2 if\cf4  file_key.endswith(\cf9 '.json'\cf4 ):\cb1 \
\cb3                 obj = s3.get_object(\cf7 Bucket\cf4 =Bucket, \cf7 Key\cf4 =file_key)\cb1 \
\cb3                 content = obj[\cf9 'Body'\cf4 ].read()\cb1 \
\cb3                 jsonObject = json.loads(content)\cb1 \
\cb3                 spotify_data.append(jsonObject)\cb1 \
\cb3                 spotify_keys.append(file_key)\cb1 \
\
\cb3     \cf12 # Extract and flatten data\cf4 \cb1 \
\cb3     all_album_rows = []\cb1 \
\cb3     all_artist_rows = []\cb1 \
\cb3     all_song_rows = []\cb1 \
\
\cb3     \cf2 for\cf4  data \cf2 in\cf4  spotify_data:\cb1 \
\cb3         all_album_rows.extend(album(data))\cb1 \
\cb3         all_artist_rows.extend(artist(data))\cb1 \
\cb3         all_song_rows.extend(song(data))\cb1 \
\
\cb3     \cf12 # Create DataFrames\cf4 \cb1 \
\cb3     album_df = pd.DataFrame.from_dict(all_album_rows).drop_duplicates(\cf7 subset\cf4 =[\cf9 'album_id'\cf4 ])\cb1 \
\cb3     artist_df = pd.DataFrame.from_dict(all_artist_rows).drop_duplicates(\cf7 subset\cf4 =[\cf9 'artist_id'\cf4 ])\cb1 \
\cb3     song_df = pd.DataFrame.from_dict(all_song_rows)\cb1 \
\
\cb3     \cf12 # Handle release_date conversion safely\cf4 \cb1 \
\cb3     \cf2 if\cf4  \cf9 'release_date'\cf4  \cf5 in\cf4  album_df.columns:\cb1 \
\cb3         album_df[\cf9 'release_date'\cf4 ] = pd.to_datetime(album_df[\cf9 'release_date'\cf4 ], \cf7 errors\cf4 =\cf9 'coerce'\cf4 )\cb1 \
\cb3     \cf2 else\cf4 :\cb1 \
\cb3         \cf6 print\cf4 (\cf9 "Warning: 'release_date' column missing from album_df"\cf4 )\cb1 \
\
\cb3     \cf12 # Convert song_added date\cf4 \cb1 \
\cb3     \cf2 if\cf4  \cf9 'song_added'\cf4  \cf5 in\cf4  song_df.columns:\cb1 \
\cb3         song_df[\cf9 'song_added'\cf4 ] = pd.to_datetime(song_df[\cf9 'song_added'\cf4 ], \cf7 errors\cf4 =\cf9 'coerce'\cf4 )\cb1 \
\
\cb3     \cf12 # Upload CSVs\cf4 \cb1 \
\cb3     timestamp = datetime.now().strftime(\cf9 "%Y-%m-\cf5 %d\cf9 _%H-%M-%S"\cf4 )\cb1 \
\
\cb3     \cf5 def\cf4  \cf6 upload_df_to_s3\cf4 (\cf7 df\cf4 , \cf7 key_prefix\cf4 ):\cb1 \
\cb3         buffer = StringIO()\cb1 \
\cb3         df.to_csv(buffer, \cf7 index\cf4 =\cf5 False\cf4 )\cb1 \
\cb3         s3.put_object(\cf7 Bucket\cf4 =Bucket, \cf7 Key\cf4 =\cf5 f\cf9 "\cf5 \{\cf4 key_prefix\cf5 \}\cf9 _\cf5 \{\cf4 timestamp\cf5 \}\cf9 .csv"\cf4 , \cf7 Body\cf4 =buffer.getvalue())\cb1 \
\
\cb3     upload_df_to_s3(song_df, \cf9 "transformed_data/songs_data/song_transformed"\cf4 )\cb1 \
\cb3     upload_df_to_s3(album_df, \cf9 "transformed_data/album_data/album_transformed"\cf4 )\cb1 \
\cb3     upload_df_to_s3(artist_df, \cf9 "transformed_data/artist_data/artist_transformed"\cf4 )\cb1 \
\
\cb3     \cf12 # Move each processed file to processed/\cf4 \cb1 \
\cb3     \cf2 for\cf4  key \cf2 in\cf4  spotify_keys:\cb1 \
\cb3         copy_source = \{\cf9 'Bucket'\cf4 : Bucket, \cf9 'Key'\cf4 : key\}\cb1 \
\cb3         new_key = \cf5 f\cf9 "raw_data/processed/\cf5 \{\cf4 key.split(\cf9 '/'\cf4 )[-\cf11 1\cf4 ]\cf5 \}\cf9 "\cf4 \cb1 \
\cb3         s3_resource.meta.client.copy(copy_source, Bucket, new_key)\cb1 \
\cb3         s3_resource.Object(Bucket, key).delete()\cb1 \
\
\cb3     \cf12 # Final cleanup: remove leftover files or folder marker from /to_processed/\cf4 \cb1 \
\cb3     leftover = s3.list_objects_v2(\cf7 Bucket\cf4 =Bucket, \cf7 Prefix\cf4 =Prefix)\cb1 \
\cb3     \cf2 if\cf4  \cf9 'Contents'\cf4  \cf5 in\cf4  leftover:\cb1 \
\cb3         \cf2 for\cf4  obj \cf2 in\cf4  leftover[\cf9 'Contents'\cf4 ]:\cb1 \
\cb3             s3.delete_object(\cf7 Bucket\cf4 =Bucket, \cf7 Key\cf4 =obj[\cf9 'Key'\cf4 ])\cb1 \
\
\cb3     \cf2 return\cf4  \{\cb1 \
\cb3         \cf9 'statusCode'\cf4 : \cf11 200\cf4 ,\cb1 \
\cb3         \cf9 'body'\cf4 : \cf5 f\cf9 "Processed \cf5 \{\cf6 len\cf4 (spotify_keys)\cf5 \}\cf9  file(s), and cleaned up to_processed/"\cf4 \cb1 \
\cb3     \}\cb1 \
\
}