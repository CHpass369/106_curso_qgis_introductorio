/* ============================================================
   LABORATORIO INTERACTIVO DE LATITUD Y LONGITUD
   Curso Introductorio QGIS

   Archivo:
   docs/assets/js/latlon.js

   Dependencias LOCALES:
   - assets/vendor/d3.v7.min.js
   - assets/data/ne_110m_land.geojson

   No requiere recursos externos durante la ejecución.
   ============================================================ */

(() => {
  "use strict";


  /* ============================================================
     1. CONFIGURACIÓN GENERAL
     ============================================================ */

  let worldLand = null;
  let worldPromise = null;


  /*
   * Capturamos la ubicación de este mismo JS.
   *
   * Si estamos en:
   *
   * /curso-qgis/assets/js/latlon.js
   *
   * el GeoJSON estará automáticamente en:
   *
   * /curso-qgis/assets/data/ne_110m_land.geojson
   */

  const SCRIPT_URL =
    document.currentScript?.src || "";

  const WORLD_URL =
    SCRIPT_URL
      ? new URL(
          "../data/ne_110m_land.geojson",
          SCRIPT_URL
        ).href
      : "assets/data/ne_110m_land.geojson";


  /* ============================================================
     2. UTILIDADES
     ============================================================ */

  function clamp(value, min, max) {
    return Math.min(
      Math.max(value, min),
      max
    );
  }


  function formatNumber(value) {
    const absolute =
      Math.abs(value);

    if (absolute < 0.005) {
      return "0.00";
    }

    return absolute.toFixed(2);
  }


  /* ============================================================
     3. GRADOS DECIMALES → DMS
     ============================================================ */

  function decimalToDMS(value, type) {

    const absolute =
      Math.abs(value);

    let degrees =
      Math.floor(absolute);

    const minutesFloat =
      (absolute - degrees) * 60;

    let minutes =
      Math.floor(minutesFloat);

    let seconds =
      (minutesFloat - minutes) * 60;


    seconds =
      Math.round(seconds * 10) / 10;


    if (seconds >= 60) {

      seconds = 0;
      minutes += 1;

    }


    if (minutes >= 60) {

      minutes = 0;
      degrees += 1;

    }


    let hemisphere = "";


    if (type === "lat") {

      if (value > 0) {
        hemisphere = "N";
      }

      else if (value < 0) {
        hemisphere = "S";
      }

    }


    if (type === "lon") {

      if (value > 0) {
        hemisphere = "E";
      }

      else if (value < 0) {
        hemisphere = "O";
      }

    }


    return (
      `${degrees}° ` +
      `${minutes}′ ` +
      `${seconds.toFixed(1)}″ ` +
      hemisphere
    ).trim();
  }


  /* ============================================================
     4. DECIMAL + HEMISFERIO
     ============================================================ */

  function decimalWithHemisphere(
    value,
    type
  ) {

    let hemisphere = "";


    if (type === "lat") {

      if (value > 0) {
        hemisphere = "N";
      }

      else if (value < 0) {
        hemisphere = "S";
      }

    }


    if (type === "lon") {

      if (value > 0) {
        hemisphere = "E";
      }

      else if (value < 0) {
        hemisphere = "O";
      }

    }


    if (Math.abs(value) < 0.005) {
      return "0.00°";
    }


    return (
      `${formatNumber(value)}° ` +
      hemisphere
    );
  }


  /* ============================================================
     5. CARGAR NATURAL EARTH
     ============================================================ */

  async function loadWorldLand() {

    if (worldLand) {
      return worldLand;
    }


    if (worldPromise) {
      return worldPromise;
    }


    worldPromise =
      fetch(WORLD_URL)

        .then(response => {

          if (!response.ok) {

            throw new Error(
              "No se pudo cargar el GeoJSON: " +
              response.status
            );

          }

          return response.json();

        })

        .then(data => {

          if (
            data.type !==
            "FeatureCollection"
          ) {

            throw new Error(
              "El archivo Natural Earth no " +
              "es un FeatureCollection válido."
            );

          }


          worldLand = data;

          return data;

        })

        .catch(error => {

          worldPromise = null;

          throw error;

        });


    return worldPromise;
  }


  /* ============================================================
     6. GEOJSON DE UN PARALELO
     ============================================================ */

  function makeParallel(latitude) {

    const coordinates = [];


    for (
      let longitude = -180;
      longitude <= 180;
      longitude += 1
    ) {

      coordinates.push([
        longitude,
        latitude
      ]);

    }


    return {
      type: "LineString",
      coordinates
    };
  }


  /* ============================================================
     7. GEOJSON DE UN MERIDIANO
     ============================================================ */

  function makeMeridian(longitude) {

    const coordinates = [];


    for (
      let latitude = -89.9;
      latitude <= 89.9;
      latitude += 1
    ) {

      coordinates.push([
        longitude,
        latitude
      ]);

    }


    return {
      type: "LineString",
      coordinates
    };
  }


  /* ============================================================
     8. ARCO SVG 2D
     ============================================================ */

  function screenArc(
    cx,
    cy,
    radius,
    startDegrees,
    endDegrees
  ) {

    const points = [];

    const difference =
      endDegrees - startDegrees;

    const steps =
      Math.max(
        3,
        Math.ceil(
          Math.abs(difference) / 3
        )
      );


    for (
      let i = 0;
      i <= steps;
      i++
    ) {

      const degrees =
        startDegrees +
        difference * (i / steps);

      const radians =
        degrees *
        Math.PI / 180;

      const x =
        cx +
        radius *
        Math.cos(radians);

      const y =
        cy -
        radius *
        Math.sin(radians);


      points.push([
        x,
        y
      ]);

    }


    return points
      .map(
        (point, index) =>
          `${index === 0 ? "M" : "L"} ` +
          `${point[0].toFixed(2)} ` +
          `${point[1].toFixed(2)}`
      )
      .join(" ");
  }


  /* ============================================================
     9. PROYECCIÓN PARA LATITUD
     ============================================================

     Esta vista está orientada para enseñar φ.

     El punto P se ubica aproximadamente sobre
     el borde derecho del globo.

     De esta forma:

     Ecuador ─────────→ P cuando φ = 0°

     y el ángulo respecto al ecuador se puede
     comprender visualmente.
     ============================================================ */

  function createLatitudeProjection(
    longitude,
    width,
    height
  ) {

    const radius =
      Math.min(
        width,
        height
      ) * 0.355;


    /*
     * Miramos la Tierra desde 90° al oeste
     * del meridiano del punto.
     *
     * Eso coloca P aproximadamente sobre
     * el perfil derecho del globo.
     */

    const centerLongitude =
      longitude - 90;


    return d3
      .geoOrthographic()

      .translate([
        width / 2,
        height / 2 - 5
      ])

      .scale(radius)

      .rotate([
        -centerLongitude,
        0,
        0
      ])

      .clipAngle(90)

      .precision(0.15);
  }


  /* ============================================================
     10. PROYECCIÓN PARA LONGITUD
     ============================================================

     Vista desde el Polo Norte.
     ============================================================ */

  function createLongitudeProjection(
    width,
    height
  ) {

    const radius =
      Math.min(
        width,
        height
      ) * 0.355;


    return d3
      .geoOrthographic()

      .translate([
        width / 2,
        height / 2 - 5
      ])

      .scale(radius)

      /*
       * Centro geográfico:
       * Polo Norte.
       */

      .rotate([
        0,
        -90,
        0
      ])

      .clipAngle(90)

      .precision(0.15);
  }


  /* ============================================================
     11. VISTA DE LATITUD
     ============================================================ */

  function renderLatitudeSVG(
    latitude,
    longitude,
    land
  ) {

    const width = 420;
    const height = 335;


    const projection =
      createLatitudeProjection(
        longitude,
        width,
        height
      );


    const path =
      d3.geoPath(projection);


    const sphere =
      path({
        type: "Sphere"
      });


    const landPath =
      path(land);


    /*
     * Retícula cada 30°.
     */

    const graticule =
      d3.geoGraticule()
        .step([
          30,
          30
        ]);


    const graticulePath =
      path(
        graticule()
      );


    const equatorPath =
      path(
        makeParallel(0)
      );


    const parallelPath =
      path(
        makeParallel(latitude)
      );


    const meridianPath =
      path(
        makeMeridian(longitude)
      );


    /*
     * Coordenada proyectada de P.
     */

    const point =
      projection([
        longitude,
        latitude
      ]);


    const px =
      point?.[0] ??
      width / 2;


    const py =
      point?.[1] ??
      height / 2;


    const cx =
      width / 2;


    const cy =
      height / 2 - 5;


    /*
     * En esta orientación P queda en el
     * perfil derecho.

     * El radio conceptual permite visualizar φ.
     */

    const angleRadius = 45;


    /*
     * SVG utiliza Y positiva hacia abajo,
     * por eso el signo se maneja aquí.
     */

    const arc =
      screenArc(
        cx,
        cy,
        angleRadius,
        0,
        latitude
      );


    const middleAngle =
      latitude / 2;


    const middleRadians =
      middleAngle *
      Math.PI / 180;


    const phiX =
      cx +
      (angleRadius + 17) *
      Math.cos(middleRadians);


    const phiY =
      cy -
      (angleRadius + 17) *
      Math.sin(middleRadians);


    let hemisphere =
      "Ecuador";


    if (latitude > 0) {
      hemisphere =
        "Hemisferio Norte";
    }

    else if (latitude < 0) {
      hemisphere =
        "Hemisferio Sur";
    }


    return `
      <svg
        class="latlon-svg"
        viewBox="0 0 ${width} ${height}"
        role="img"
        aria-label="Representación geográfica de la latitud"
      >

        <!-- Océano -->
        <path
          class="latlon-ocean"
          d="${sphere || ""}"
        />


        <!-- Retícula -->
        <path
          class="latlon-graticule"
          d="${graticulePath || ""}"
        />


        <!-- Continentes Natural Earth -->
        <path
          class="latlon-land"
          d="${landPath || ""}"
        />


        <!-- Ecuador -->
        <path
          class="latlon-equator"
          d="${equatorPath || ""}"
        />


        <!-- Paralelo de P -->
        <path
          class="latlon-current-parallel"
          d="${parallelPath || ""}"
        />


        <!-- Meridiano de P -->
        <path
          class="latlon-current-meridian"
          d="${meridianPath || ""}"
        />


        <!-- Radio -->
        <line
          class="latlon-angle-line"
          x1="${cx}"
          y1="${cy}"
          x2="${px}"
          y2="${py}"
        />


        <!-- Arco φ -->
        <path
          class="latlon-angle-arc"
          d="${arc}"
        />


        <!-- Centro -->
        <circle
          class="latlon-center"
          cx="${cx}"
          cy="${cy}"
          r="3.5"
        />


        <!-- Punto P -->
        <circle
          class="latlon-point"
          cx="${px}"
          cy="${py}"
          r="6"
        />


        <text
          class="latlon-point-label"
          x="${px + 10}"
          y="${py - 8}"
        >
          P
        </text>


        <!-- φ -->
        <text
          class="latlon-angle-label"
          x="${phiX}"
          y="${phiY}"
          text-anchor="middle"
        >
          φ
        </text>


        <text
          class="latlon-pole-label"
          x="${cx}"
          y="18"
          text-anchor="middle"
        >
          Polo Norte
        </text>


        <text
          class="latlon-pole-label"
          x="${cx}"
          y="${height - 37}"
          text-anchor="middle"
        >
          Polo Sur
        </text>


        <text
          class="latlon-result"
          x="${cx}"
          y="${height - 10}"
          text-anchor="middle"
        >
          Latitud:
          ${decimalWithHemisphere(
            latitude,
            "lat"
          )}
          ·
          ${hemisphere}
        </text>

      </svg>
    `;
  }


  /* ============================================================
     12. VISTA DE LONGITUD
     ============================================================ */

  function renderLongitudeSVG(
    latitude,
    longitude,
    land
  ) {

    const width = 420;
    const height = 335;


    const projection =
      createLongitudeProjection(
        width,
        height
      );


    const path =
      d3.geoPath(projection);


    const sphere =
      path({
        type: "Sphere"
      });


    const landPath =
      path(land);


    const graticule =
      d3.geoGraticule()
        .step([
          30,
          30
        ]);


    const graticulePath =
      path(
        graticule()
      );


    const greenwichPath =
      path(
        makeMeridian(0)
      );


    const currentMeridianPath =
      path(
        makeMeridian(longitude)
      );


    const parallelPath =
      path(
        makeParallel(latitude)
      );


    const point =
      projection([
        longitude,
        latitude
      ]);


    const px =
      point?.[0] ??
      width / 2;


    const py =
      point?.[1] ??
      height / 2;


    const cx =
      width / 2;


    const cy =
      height / 2 - 5;


    /*
     * Etiqueta λ entre Polo Norte y P.
     */

    const lambdaX =
      cx +
      (px - cx) * 0.54 +
      11;


    const lambdaY =
      cy +
      (py - cy) * 0.54 -
      8;


    let hemisphere =
      "Greenwich";


    if (longitude > 0) {
      hemisphere =
        "Longitud Este";
    }

    else if (longitude < 0) {
      hemisphere =
        "Longitud Oeste";
    }


    return `
      <svg
        class="latlon-svg"
        viewBox="0 0 ${width} ${height}"
        role="img"
        aria-label="Representación geográfica de la longitud"
      >

        <!-- Océano -->
        <path
          class="latlon-ocean"
          d="${sphere || ""}"
        />


        <!-- Retícula -->
        <path
          class="latlon-graticule"
          d="${graticulePath || ""}"
        />


        <!-- Continentes Natural Earth -->
        <path
          class="latlon-land"
          d="${landPath || ""}"
        />


        <!-- Paralelo correspondiente a P -->
        <path
          class="latlon-current-parallel"
          d="${parallelPath || ""}"
        />


        <!-- Greenwich -->
        <path
          class="latlon-greenwich"
          d="${greenwichPath || ""}"
        />


        <!-- Meridiano correspondiente a P -->
        <path
          class="latlon-current-meridian"
          d="${currentMeridianPath || ""}"
        />


        <!-- Polo Norte -->
        <circle
          class="latlon-center"
          cx="${cx}"
          cy="${cy}"
          r="4"
        />


        <!-- Punto P -->
        <circle
          class="latlon-point"
          cx="${px}"
          cy="${py}"
          r="6"
        />


        <text
          class="latlon-point-label"
          x="${px + 10}"
          y="${py - 8}"
        >
          P
        </text>


        <!-- λ -->
        <text
          class="latlon-angle-label"
          x="${lambdaX}"
          y="${lambdaY}"
        >
          λ
        </text>


        <text
          class="latlon-center-label"
          x="${cx}"
          y="${cy + 18}"
          text-anchor="middle"
        >
          Polo Norte
        </text>


        <text
          class="latlon-greenwich-label"
          x="${cx}"
          y="18"
          text-anchor="middle"
        >
          Greenwich 0°
        </text>


        <text
          class="latlon-direction-label"
          x="36"
          y="${cy}"
          text-anchor="middle"
        >
          Oeste
        </text>


        <text
          class="latlon-direction-label"
          x="${width - 36}"
          y="${cy}"
          text-anchor="middle"
        >
          Este
        </text>


        <text
          class="latlon-result"
          x="${cx}"
          y="${height - 10}"
          text-anchor="middle"
        >
          Longitud:
          ${decimalWithHemisphere(
            longitude,
            "lon"
          )}
          ·
          ${hemisphere}
        </text>

      </svg>
    `;
  }


  /* ============================================================
     13. CREAR PANEL NUMÉRICO
     ============================================================ */

  function renderReadout(
    element,
    latitude,
    longitude
  ) {

    let latitudeHemisphere =
      "Ecuador";


    if (latitude > 0) {
      latitudeHemisphere =
        "Norte";
    }

    else if (latitude < 0) {
      latitudeHemisphere =
        "Sur";
    }


    let longitudeHemisphere =
      "Greenwich";


    if (longitude > 0) {
      longitudeHemisphere =
        "Oriental";
    }

    else if (longitude < 0) {
      longitudeHemisphere =
        "Occidental";
    }


    element.innerHTML = `

      <div class="latlon-coordinate-card">

        <span
          class="latlon-coordinate-symbol"
        >
          φ
        </span>

        <div>

          <span
            class="latlon-coordinate-name"
          >
            Latitud
          </span>

          <strong>
            ${decimalWithHemisphere(
              latitude,
              "lat"
            )}
          </strong>

          <small>
            ${decimalToDMS(
              latitude,
              "lat"
            )}
          </small>

        </div>

      </div>


      <div class="latlon-coordinate-card">

        <span
          class="latlon-coordinate-symbol"
        >
          λ
        </span>

        <div>

          <span
            class="latlon-coordinate-name"
          >
            Longitud
          </span>

          <strong>
            ${decimalWithHemisphere(
              longitude,
              "lon"
            )}
          </strong>

          <small>
            ${decimalToDMS(
              longitude,
              "lon"
            )}
          </small>

        </div>

      </div>


      <div class="latlon-hemisphere">

        <span>
          Hemisferios:
        </span>

        <strong>
          ${latitudeHemisphere}
          ·
          ${longitudeHemisphere}
        </strong>

      </div>
    `;
  }


  /* ============================================================
     14. INICIALIZAR UN LABORATORIO
     ============================================================ */

  async function initializeLab(lab) {

    if (
      lab.dataset.latlonInitialized ===
      "true"
    ) {
      return;
    }


    lab.dataset.latlonInitialized =
      "true";


    const latitudeInput =
      lab.querySelector(
        "[data-latitude]"
      );


    const longitudeInput =
      lab.querySelector(
        "[data-longitude]"
      );


    if (
      !latitudeInput ||
      !longitudeInput
    ) {

      console.warn(
        "LatLon: faltan los controles."
      );

      return;
    }


    /* ----------------------------------------------------------
       Comprobar D3 local
       ---------------------------------------------------------- */

    if (
      typeof window.d3 ===
      "undefined"
    ) {

      lab.innerHTML = `
        <div class="latlon-error">
          No se pudo cargar D3 local.
        </div>
      `;

      return;
    }


    /* ----------------------------------------------------------
       Valores iniciales
       ---------------------------------------------------------- */

    if (!latitudeInput.value) {
      latitudeInput.value =
        "-17.39";
    }


    if (!longitudeInput.value) {
      longitudeInput.value =
        "-66.16";
    }


    /* ----------------------------------------------------------
       Crear área visual
       ---------------------------------------------------------- */

    let visual =
      lab.querySelector(
        ".latlon-visual"
      );


    if (!visual) {

      visual =
        document.createElement("div");

      visual.className =
        "latlon-visual";

      lab.prepend(visual);

    }


    visual.innerHTML = `

      <section class="latlon-panel">

        <header class="latlon-panel-title">

          <span class="latlon-panel-symbol">
            φ
          </span>

          Latitud

        </header>

        <div
          class="latlon-map-container"
          data-latitude-svg
        >
          <div class="latlon-loading">
            Cargando superficie terrestre…
          </div>
        </div>

      </section>


      <section class="latlon-panel">

        <header class="latlon-panel-title">

          <span class="latlon-panel-symbol">
            λ
          </span>

          Longitud

        </header>

        <div
          class="latlon-map-container"
          data-longitude-svg
        >
          <div class="latlon-loading">
            Cargando superficie terrestre…
          </div>
        </div>

      </section>
    `;


    const latitudeContainer =
      visual.querySelector(
        "[data-latitude-svg]"
      );


    const longitudeContainer =
      visual.querySelector(
        "[data-longitude-svg]"
      );


    /* ----------------------------------------------------------
       Crear readout
       ---------------------------------------------------------- */

    let readout =
      lab.querySelector(
        ".latlon-readout"
      );


    if (!readout) {

      readout =
        document.createElement("div");

      readout.className =
        "latlon-readout";


      const controls =
        lab.querySelector(
          ".latlon-controls"
        );


      if (controls) {
        controls.after(readout);
      }

      else {
        lab.append(readout);
      }

    }


    /* ----------------------------------------------------------
       Cargar Natural Earth
       ---------------------------------------------------------- */

    let land;


    try {

      land =
        await loadWorldLand();

    }

    catch (error) {

      console.error(
        "LatLon:",
        error
      );


      const message = `
        <div class="latlon-error">
          No se pudo cargar
          ne_110m_land.geojson.
        </div>
      `;


      latitudeContainer.innerHTML =
        message;


      longitudeContainer.innerHTML =
        message;


      return;
    }


    /* ==========================================================
       RENDER
       ========================================================== */

    function render() {

      let latitude =
        parseFloat(
          latitudeInput.value
        );


      let longitude =
        parseFloat(
          longitudeInput.value
        );


      if (
        !Number.isFinite(latitude)
      ) {
        latitude = 0;
      }


      if (
        !Number.isFinite(longitude)
      ) {
        longitude = 0;
      }


      latitude =
        clamp(
          latitude,
          -90,
          90
        );


      longitude =
        clamp(
          longitude,
          -180,
          180
        );


      latitudeInput.value =
        latitude;


      longitudeInput.value =
        longitude;


      latitudeContainer.innerHTML =
        renderLatitudeSVG(
          latitude,
          longitude,
          land
        );


      longitudeContainer.innerHTML =
        renderLongitudeSVG(
          latitude,
          longitude,
          land
        );


      renderReadout(
        readout,
        latitude,
        longitude
      );
    }


    /* ----------------------------------------------------------
       Eventos
       ---------------------------------------------------------- */

    latitudeInput.addEventListener(
      "input",
      render
    );


    longitudeInput.addEventListener(
      "input",
      render
    );


    latitudeInput.addEventListener(
      "change",
      render
    );


    longitudeInput.addEventListener(
      "change",
      render
    );


    render();
  }


  /* ============================================================
     15. INICIALIZAR TODOS
     ============================================================ */

  function initializeAll() {

    document
      .querySelectorAll(
        ".latlon-lab"
      )
      .forEach(
        initializeLab
      );

  }


  if (
    document.readyState ===
    "loading"
  ) {

    document.addEventListener(
      "DOMContentLoaded",
      initializeAll
    );

  }

  else {

    initializeAll();

  }


  /*
   * MkDocs Material
   * navigation.instant
   */

  if (
    typeof window.document$ !==
      "undefined" &&
    window.document$ &&
    typeof window.document$.subscribe ===
      "function"
  ) {

    window.document$.subscribe(
      initializeAll
    );

  }

})();