<script>
    import { writable } from "svelte/store";
    import FileInsert from "./FileInsert.svelte";
    import Uploaded from "./Uploaded.svelte";
    import UploadButton from "./UploadButton.svelte";
  
    let f = writable([]);
  </script>
  
  <div class="bg-white rounded-lg min-h-[50vh]">
    <p class="font-bold justify-center flex text-2xl m-4">Upload</p>
    <FileInsert bind:files={f} />
    <Uploaded name={$f} />
    <UploadButton/>
  </div>
  