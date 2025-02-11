import { useEffect ,useState} from "react"
import { useDispatch, useSelector } from "react-redux"
import {getCurrentAllSongs} from '../../redux/songs'
import { useNavigate, useParams } from "react-router-dom"
import './SongDetail.css'
import { FaPlay } from 'react-icons/fa';

function SongDetail(){
  const {song_id} = useParams()
  const navigate = useNavigate()
  const [visible_lyrics,setVisible_lyrics] = useState(6)
  
  const dispatch = useDispatch()
  useEffect(()=>{
      dispatch(getCurrentAllSongs())
  },[dispatch])

  const songs = useSelector(state=>state.song.currentUserAllSongs)
  const song= songs.filter(el=>el.id===Number(song_id))[0]
//   const album_song=song.albums[0].songs
//   console.log('the song ', songs,song,song_id,album_song )

    return (
        <div>
            <div>
                <button onClick={()=> navigate('/songs/new')}>add a song</button>
            </div>
        {
              song?
              <div className='song_details'>
                  <div className="song_head">
                  <img className='img_song_detail' src={song.image_url}></img>
                  <div >
                  <h1>{song.title}</h1>
                   <p>{song.release_year} {  '.'  } {song.duration}</p>
        
                  </div>
                  </div>
              <div className='song_body'>
                <p>Lyrics</p>
               <div>
               {
               song.lyrics.split(',').slice(0,visible_lyrics).map((el,index)=> 
               (<p key ={index}>{el}</p>)
            )}
            </div>
            {
                visible_lyrics===6?
                <button onClick={()=>setVisible_lyrics(song.lyrics.length)} className="visible_lyrics">... show more</button>
                :
                <button onClick={()=>setVisible_lyrics(6)} className="visible_lyrics">show less</button>

            }
           
              </div>
              <div className='song_foot'>
              {/* <audio controls >
                  <source  src={song.audio_url} type='audio/mp3' />
              </audio> */}
              </div>
              <div>
                <table  className="tableSongList">
                    <thead>
                        <tr className="tableHead">
                            <th></th>
                            <th>Title</th>
                            <th>Artist</th>
                            <th>🕘</th>
                        </tr>

                    </thead>
                    <tbody >
                        {
                            song.albums.length !==0?
                           song.albums[0].songs.map((el,index)=>(
                            <tr key={index} className="tableBody">
                                <td>
                                    <button style={{backgroundColor:"transparent"}} ><FaPlay size={15} color="darkgreen"  /></button>
                                </td>
                                <td>{el.title}</td>
                                <td>{song.albums[0].artist.artist_name}</td>
                                <td>{el.duration}</td>

                            </tr>
                           )) 
                           :null
                        }
                    </tbody>
                </table>

              </div>
          
                 
              </div>
              :null
        }
        </div>
    )
}
export default SongDetail