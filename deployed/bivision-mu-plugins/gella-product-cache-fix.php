<?php
/**
 * Plugin Name: GelLa Product Cache Fix
 * Description: Normalizes Cache-Control on bevision_product singles for guests so WP Super Cache stores them. Fixes stray "max-age=300" (bifinance/bidebitors/bimedical). 2026-05-29 GelLa.
 *
 * MIRROR of LIVE file: bivision.ge:/home/bivision/public_html/wp-content/mu-plugins/gella-product-cache-fix.php
 * Deployed 2026-05-29 via cPanel UAPI (no server git). Rollback = delete the live file (<30s, visitor-invisible).
 * Result: bidebitors 1.2s->61ms, bimedical 1.2s->67ms (WPSC-cached). bifinance header cleaned but still uncached (separate DONOTCACHEPAGE trigger - unresolved).
 */
if (!defined('ABSPATH')) { exit; }
function gella_pcf_clean_cc() {
    if (headers_sent()) { return; }
    header_remove('Cache-Control');
    header_remove('Pragma');
    header_remove('Expires');
    header('Cache-Control: max-age=3600, public');
}
add_action('send_headers', function () {
    if (is_singular('bevision_product') && !is_user_logged_in()) { gella_pcf_clean_cc(); }
}, PHP_INT_MAX);
add_action('template_redirect', function () {
    if (is_singular('bevision_product') && !is_user_logged_in()) { header_register_callback('gella_pcf_clean_cc'); }
});
