import pygame
import os
from CircularDoublyLinkedList.Music_Project.playList import CircularDoublyLinkedList

class musicPlayer:
    def __init__(self):
        self.play_list=CircularDoublyLinkedList()
        self.current_song=""
        pygame.mixer.init()
    
    def load_music_folder(self,folder_path):
        if folder_path:
            extension=('.mp3', '.wav', '.ogg')
            for file in os.listdir(folder_path):
                if file.endswith(extension):
                    join_filepath=os.path.join(folder_path,file)
                    self.play_list.add_song(join_filepath)
            if self.play_list.head:
                self.play_list.current=self.play_list.head
                self.current_song=self.play_list.head.song_path

    def play_music(self):
        if not self.play_list.head:
            print("No song is available")
            return
        print(f"Current song: {self.current_song}")
        pygame.mixer_music.load(self.current_song)
        pygame.mixer_music.play()
        print("---------------------Music is playing---------------------")

    def pause_music(self):
        if not self.play_list.head:
            print("No song is available")
            return
        pygame.mixer_music.pause()
        print("---------------------pause the music---------------------")

    def resume_music(self):
        if not self.play_list.head:
            print("No song is available")
            return
        pygame.mixer_music.unpause()
        print("---------------------resume the music---------------------")

    def stop_music(self):
        if not self.play_list.head:
            print("No song is available")
            return
        pygame.mixer_music.stop()
        print("---------------------stop the music---------------------")
    
    def next_song(self):
        if not self.play_list.head:
            print("No song is available")
            return
        print("---------------------Next song---------------------")
        self.current_song = self.play_list.next_song()
        self.play_music()
    
    def prev_song(self):
        if not self.play_list.head:
            print("No song is available")
            return
        print("---------------------Next song---------------------")
        self.current_song = self.play_list.prev_song()
        self.play_music()

    def main(self):
        self.load_music_folder("D:\Christian songs\All Time")
        while True:
            commend=input("""---------------------------------------------
Enter the commend: 
1. Play - Play the music.
2. Pause - Pause the music.
3. Resume - Resume the music.
4. Stop - Stop the music.
5. Prev - Prev music.
6. Next - Next music.
7. Display - Display the song.
8. Quit - Quit
---------------------------------------------
""")
            if commend.lower() in "play":
                print("play")
                self.play_music()
            
            elif "pause" in commend.lower():
                self.pause_music()

            elif "resume" in commend.lower():
                self.resume_music()
            
            elif "stop" in commend.lower():
                self.stop_music()
            
            elif "next" in commend.lower():
                self.next_song()

            elif "prev" in commend.lower():
                self.prev_song()
            
            elif "display" in commend.lower():
                self.play_list.display_playlist()

            elif commend.lower() in "quit":
                break

            else:
                print("Invalid commend")
            

if __name__=='__main__':
    mp=musicPlayer()
    mp.main()
