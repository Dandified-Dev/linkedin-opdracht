<script>
	import { writable } from "svelte/store";
	import CloudIcon from "../../assets/cloud-upload.svg";
  
	let fileIdCounter = 0; // Initialize the fileIdCounter
  
	export let files = writable([]);
  
	function uploadFile(event) {
	  event.preventDefault();
	  const uploadedFiles = Array.from(event.target.files || event.dataTransfer.files).map(file => ({
		id: fileIdCounter++, // Assign a unique ID to each file
		file
	  }));
	  files.update(existingFiles => [...existingFiles, ...uploadedFiles]);
	}
  
	function handleDragOver(event) {
	  event.preventDefault();
	}
  </script>
  
  <!-- svelte-ignore a11y-no-static-element-interactions -->
  <div 
	aria-label="Drag and drop file upload" 
	class="border border-black border-dashed p-3 mx-12 my-8 rounded-md bg-[#F8F8FF] items-center flex flex-col" 
	on:drop={uploadFile} 
	on:dragover={handleDragOver}
  >
	<img src={CloudIcon} alt="cloud upload icon" class="w-20 h-20" />
	<label class="font-bold" for="avatar">Drag & drop files or 
	  <span class="underline cursor-pointer text-[#483EA8]">Browse</span>
	  <input 
		accept=".csv, text/csv" 
		id="avatar" 
		name="avatar" 
		type="file" 
		class="hidden" 
		on:change={uploadFile} 
	  />
	</label>
	<p>Supported format: CSV</p>
  </div>
  