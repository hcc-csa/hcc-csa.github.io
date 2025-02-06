import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders'; // Not available with legacy API

const events = defineCollection({
  loader: file("src/collections/events.json"),
  schema: z.object({
    title: z.string(),
    slug: z.url(),
	location: z.object({
		name: z.string(),
		link: z.url(),
	}),
    event_datetime: z.string().datetime(),
    event_duration: z.string().duration(),
    type: z.enum(['In-Person', 'Hybrid', 'Virtual']),
	description: z.string().optional(),
    image: z.url().optional(),
	registration_link: z.url().optional(),
  }),
});

export const collections = { events };