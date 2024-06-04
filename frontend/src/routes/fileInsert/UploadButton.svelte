<script>
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  function uploadFiles() {
    dispatch("uploadFiles");
  }
</script>

<button on:click={uploadFiles} class="bg-[#483EA8] w-[-webkit-fill-available] justify-center flex mx-12 py-4 px-3 rounded-lg text-white font-bold m-8">
  UPLOAD FILES
</button>
