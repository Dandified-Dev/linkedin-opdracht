<script>
    import Bin from "../../assets/bin.svg";
  export let name;
  function removeFile(){
    name = [];
    console.log("clicked");
  }
</script>

<div class="flex flex-col mx-12 text-2xl min-h-[20vh]">
  <p>Uploaded</p>
  {#if name.length !== 0}
  {#each Array.from(name) as file}
  <div class="flex justify-between items-center p-2 rounded-lg border-[#2EB93E] border-2 my-2">
    <p>{file.name}</p>
    <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <img on:click={removeFile} class="h-6 w-6 bg-gray-200 p-1 rounded-full" src={Bin} alt="bin"/>
  </div>
    {/each}
  {/if}
</div>
