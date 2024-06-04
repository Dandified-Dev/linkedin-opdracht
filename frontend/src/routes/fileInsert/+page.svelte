<script>
  import { writable } from "svelte/store";
  import FileInsert from "./FileInsert.svelte";
  import Uploaded from "./Uploaded.svelte";
  import UploadButton from "./UploadButton.svelte";

  let f = writable([]);
  let isUploading = writable(false); // Track the upload state

  async function sendFiles(event) {
    const files = $f;
    f.set([]);


    if (files.length === 0) {
      console.error("No files selected");
      return;
    }

    isUploading.set(true); // Set uploading state to true

    try {
      // Combine the contents of all files
      let combinedUrls = [];

      for (const { file } of files) {
        // Read the contents of the file
        const fileContent = await file.text();
        console.log(fileContent);

        // Extract URLs from the file and add to combined list
        const urls = fileContent.split('\n').map(line => line.trim()).filter(line => line);
        combinedUrls = combinedUrls.concat(urls);
      }

      const payload = JSON.stringify({ url: combinedUrls });

      // Send the combined file contents in a single fetch request
      const res = await fetch('http://127.0.0.1:8000/api/urls/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json' // Set the content type to JSON
        },
        body: payload // Send the JSON formatted data
      });

      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status}`);
      }

      const json = await res.json();
      console.log(JSON.stringify(json));

      // Clear the file input after successful upload
    } catch (error) {
      console.error('Error:', error);
    }
  }

  function deleteFile(id) {
    f.update(files => files.filter(file => file.id !== id.detail));
  }
</script>

<div class="bg-white rounded-lg min-h-[50vh] w-[-webkit-fill-available] mx-auto max-w-[64rem]">
  <p class="font-bold justify-center flex text-2xl m-4">Upload</p>
  <FileInsert bind:files={f} />
  <!-- Pass the deleteFile function as a prop to the Uploaded component -->
  <Uploaded name={$f} on:deleteFile={deleteFile} />
  <UploadButton on:uploadFiles={sendFiles}/>
</div>
