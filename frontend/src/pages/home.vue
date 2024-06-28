<template>
    <div>
        ahoy
        <p>
            E o grande prop é: {{ msg }}
        </p>
        <Link href="/subpage">Outra página</Link>
    </div>
</template>
<script setup>
import { Link } from "@inertiajs/vue3";
const props = defineProps(["msg"])

</script>