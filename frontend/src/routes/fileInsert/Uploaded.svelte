<script>
    import Bin from "../../assets/bin.svg";

  import { createEventDispatcher } from 'svelte';

  export let name = [];
  
  const dispatch = createEventDispatcher();

  function handleDelete(id) {
    console.log('Deleting file with id:', id);
    // Emit the deleteFile event with the file id
    dispatch('deleteFile', id);
  }
</script>

<div class="flex flex-col mx-12 text-2xl min-h-[20vh]">
  <p>Uploaded</p>
  {#if name.length !== 0}
    {#each name as { id, file }}
      <div
        class="flex justify-between items-center p-2 rounded-lg border-[#2EB93E] border-2 my-2"
        key={id}
      >
        <p>{file.name}</p>
        <button on:click={() => handleDelete(id)} class="h-6 w-6 bg-gray-200 p-1 rounded-full" type="button">
          <img src={Bin} alt="bin" />
        </button>

      </div>
    {/each}
  {:else}
    <p>No files uploaded.</p>
  {/if}
</div>
