<script>
  import welcome from "$lib/images/svelte-welcome.webp";
  import welcome_fallback from "$lib/images/svelte-welcome.png";
  import { onMount } from "svelte";
  import Card from "./Card.svelte";

  var apiData = [];

  onMount(async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/api/profiles");
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      apiData = data;
    } catch (error) {
      console.error("Fetch error:", error);
    }
  });
</script>

<div class="flex flex-col items-center">
  <ul class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-3 gap-4">
    {#each apiData as item}
      <li class="">
        <Card data={item} />
      </li>
    {/each}
  </ul>
</div>


<style>
</style>
