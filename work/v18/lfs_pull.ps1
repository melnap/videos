$l = Get-Content "C:\Users\49c9\Downloads\MorioStudioStarter-v0.1\MyStudio\stockedandready\work\v18\lfs_list.txt"
Set-Location "C:\Users\49c9\Downloads\MorioStudioStarter-v0.1\MyStudio\stockedandready"
& "C:\Users\49c9\AppData\Local\Programs\Git\cmd\git.exe" -c "lfs.fetchinclude=$l" lfs pull
Set-Location "C:\Users\49c9\Downloads\MorioStudioStarter-v0.1\MyStudio"
Write-Output "LFS DONE"
