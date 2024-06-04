<script>
  export let data;
  // Function to parse the string into a JavaScript object
  function parseDateString(dateString) {
    return JSON.parse(dateString.replace(/'/g, '"'));
  }

  // Function to format the date
  function getFormattedDate(dateString) {
    const dateObj = parseDateString(dateString);
    const monthNames = [
      "Januari",
      "Februari",
      "Maart",
      "April",
      "Mei",
      "Juni",
      "Juli",
      "Augustus",
      "September",
      "Oktober",
      "November",
      "December",
    ];
    const monthName = monthNames[dateObj.month - 1]; // Adjust month index
    return `${monthName} ${dateObj.year}`;
  }

</script>

<div>
  <div class="m-5 p-4 rounded-lg bg-white">
    <div class="bg-gray-200 p-2 rounded-md">
      <h2 class="font-bold text-2xl">{data.first_name} {data.last_name}</h2>
      <p class="text-xl">{data.headline}</p>
      <a href={data.url} class="text-blue-500 hover:underline">LinkedIn</a>

    </div>
    <div class="card-body">
      <div class="my-2 bg-gray-200 p-2 rounded-md">
        <p class="text-3xl">Werkervaring</p>
        {#each Array.from(data.experiences) as experience}
          <div class="border-t mt-5">
            <p class="text-lg font-bold">{experience.title}</p>
            <p>{experience.company}</p>
            <p>
              {getFormattedDate(experience.start_date)} -
              {experience.end_date ? getFormattedDate(experience.end_date) : "Heden"}
            </p>

            <p>{experience.location}</p>
          </div>
        {/each}
      </div>
      <div class="my-2 bg-gray-200 p-2 rounded-md">
        <p class="text-3xl">Opleiding</p>
        {#each Array.from(data.educations) as education}
          <div class="border-t pt-2">
            <p class="text-lg font-bold">{education.school}</p>
            {#if education.degree}
              <p>{education.degree}, {education.field_of_study}</p>
            {/if}
            <p>
              {education.start_date} - {education.end_date ? education.end_date : "Heden"}
            </p>
          </div>
        {/each}
      </div>
      <div class="my-2 bg-gray-200 p-2 rounded-md">
        <p class="text-3xl">Vaardigheden</p>
        {#each Array.from(data.skills) as skill}
          <div class="border-t pt-2">
            <p>{skill.skill_name}</p>
          </div>
        {/each}
      </div>
    </div>
  </div>
</div>

<style></style>
