<script lang="ts">
	import { searchProducts } from '$lib/api';

	let query = '';
	let results: any[] = [];
	let loading = false;
	let error = '';

	async function search() {
		if (!query.trim()) return;

		loading = true;
		error = '';

		try {
			const res = await searchProducts(query);
			results = res.items;
		} catch (e) {
			error = 'خطا در ارتباط با سرور';
		} finally {
			loading = false;
		}
	}
</script>

<div class="mx-auto max-w-3xl p-6">
	<h1 class="text-primary mb-4 text-2xl font-bold">جستجوی کالا</h1>

	<div class="mb-4 flex gap-2">
		<input
			type="text"
			placeholder="مثلاً: شیلنگ۶"
			bind:value={query}
			on:keydown={(e) => e.key === 'Enter' && search()}
			class="focus:ring-primary flex-1 rounded border p-2 shadow-sm focus:ring-2 focus:outline-none"
		/>
		<button on:click={search} class="bg-primary rounded px-4 py-2 text-white hover:bg-blue-700">
			جستجو
		</button>
	</div>

	{#if loading}
		<p class="mb-4 text-gray-500">در حال جستجو...</p>
	{/if}

	{#if error}
		<p class="text-error mb-4">{error}</p>
	{/if}

	{#if results.length > 0}
		<div class="overflow-x-auto">
			<table class="min-w-full rounded border bg-white shadow-sm">
				<thead class="bg-gray-200">
					<tr>
						<th class="px-4 py-2 text-left">کد کالا</th>
						<th class="px-4 py-2 text-left">نام کالا</th>
						<th class="px-4 py-2 text-left">محل کالا</th>
					</tr>
				</thead>
				<tbody>
					{#each results as item, i}
						<tr class={i % 2 === 0 ? 'bg-gray-50' : 'bg-white'}>
							<td class="border px-4 py-2">{item['کد کالا']}</td>
							<td class="border px-4 py-2">{item['نام کالا']}</td>
							<td class="border px-4 py-2">{item['محل کالا']}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{:else if !loading && !error}
		<p class="mt-4 text-gray-400">هیچ نتیجه‌ای یافت نشد.</p>
	{/if}
</div>

<style lang="postcss">
	@reference "tailwindcss";
	:global(html) {
		background-color: theme(--color-gray-300);
	}
</style>
